from django.http.request import RawPostDataException
import json


def get_client_ip(request):
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    return (
        x_forwarded_for.split(",")[0]
        if x_forwarded_for
        else request.META.get("REMOTE_ADDR")
    )

def get_request_data(request):
    try:
        # Attempt to parse JSON body if it's a JSON request
        return json.loads(request.body.decode("utf-8")) if request.body else {}
    except (json.JSONDecodeError, RawPostDataException):
        pass  # Ignore errors if JSON is malformed or body is already accessed

    # If DRF is used, request.data may contain parsed data
    if hasattr(request, "data"):
        return request.data

    # For form-encoded POST data
    if hasattr(request, "POST"):
        return request.POST.dict()  # Convert QueryDict to standard dict

    return {}