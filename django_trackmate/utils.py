from django.http.request import RawPostDataException


def get_client_ip(request):
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    return (
        x_forwarded_for.split(",")[0]
        if x_forwarded_for
        else request.META.get("REMOTE_ADDR")
    )

def get_request_data(request):
    try:
        return request.body
    except RawPostDataException:
        pass  # Ignore if body is already accessed

    if hasattr(request, "data"):
        return request.data
    if hasattr(request, "POST"):
        return request.POST
    return {}