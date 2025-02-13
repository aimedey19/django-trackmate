import time

from django.conf import settings

from .main import inner_tracker


class RequestTrackerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        TRACKMATE_EXCLUDED_PATH = getattr(
            settings,
            "TRACKMATE_EXCLUDED_PATH",
            ["/admin/"]
        )
        start_time = time.time()
        request._django_trackmate_middleware_tracked = True
        response = self.get_response(request)
        exec_time = time.time() - start_time
        if any(request.path.startswith(path) for path in TRACKMATE_EXCLUDED_PATH):
            return response
        kwargs = {"execution_time": exec_time}
        inner_tracker(request, response, **kwargs)
        return response