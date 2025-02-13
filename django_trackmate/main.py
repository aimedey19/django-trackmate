import time
from datetime import datetime
from functools import wraps

from .utils import get_client_ip, get_request_data

CREATE, READ, UPDATE, DELETE = "Create", "Read", "Update", "Delete"
LOGIN, LOGOUT, LOGIN_FAILED = "Login", "Logout", "Login Failed"
SUCCESS, FAILED = "Success", "Failed"
ACTION_STATUS = [(SUCCESS, SUCCESS), (FAILED, FAILED)]

action_type_mapper = {
    "GET": READ,
    "POST": CREATE,
    "PUT": UPDATE,
    "PATCH": UPDATE,
    "DELETE": DELETE,
}


def _get_action_type(request) -> str:
    return action_type_mapper.get(f"{request.method.upper()}")


def _build_log_message(request) -> str:
    return f"User: {request.user} -- Action Type: {_get_action_type(request)} -- Path: {request.path} -- Path Name: {request.resolver_match.url_name} -- IP: {get_client_ip(request)}"


def get_log_message(request, log_message: str = None) -> str:
    return log_message or _build_log_message(request)


def tracker(content_object=None):
    def inner(func):
        from .models import ActivityLog
        @wraps(func)
        def wrapper(request, *args, **kwargs):
            response = func(request, *args, **kwargs)
            if hasattr(request, "_django_trackmate_middleware_tracked"):
                return response
            start_time = time.time()
            exec_time = time.time() - start_time
            kwargs = {"execution_time": exec_time}
            if content_object:
                kwargs["content_object"] = content_object
            inner_tracker(request, response, **kwargs)
            return response

        return wrapper

    return inner


def inner_tracker(request, response, **kwargs):
    from .models import ActivityLog
    data = {
        "actor": request.user if request.user.is_authenticated else None,
        "action_type": action_type_mapper.get(request.method),
        "action_time": datetime.now(),
        "remarks": get_log_message(request),
        "status": SUCCESS if response.status_code < 400 else FAILED,
        "status_code": response.status_code,
        "response": response.data if hasattr(response, "data") else {},
        "data": get_request_data(request),
        **kwargs
    }
    ActivityLog.objects.create(**data)
