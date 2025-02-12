from datetime import datetime

from django.contrib.auth.signals import user_logged_in, user_login_failed, user_logged_out
from django.dispatch import receiver

from .models import ActivityLog, LOGIN, LOGIN_FAILED, LOGOUT
from .utils import get_client_ip


@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    message = f"{user} is logged in with ip:{get_client_ip(request)}"
    ActivityLog.objects.create(
        actor=user,
        action_type=LOGIN,
        action_time=datetime.now(),
        remarks=message
    )


@receiver(user_login_failed)
def log_user_login_failed(sender, credentials, request, **kwargs):
    message = f"Login Attempt Failed for email {credentials.get('email') or credentials.get('username')} with ip: {get_client_ip(request)}"
    ActivityLog.objects.create(
        actor=None,
        action_type=LOGIN_FAILED,
        action_time=datetime.now(),
        remarks=message
    )


@receiver(user_logged_out)
def log_user_logout(sender, request, user, **kwargs):
    message = f"{user} is logged out with ip:{get_client_ip(request)}"
    ActivityLog.objects.create(
        actor=user,
        action_type=LOGOUT,
        action_time=datetime.now(),
        remarks=message
    )