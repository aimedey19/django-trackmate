from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

User = get_user_model()

CREATE, READ, UPDATE, DELETE = "Create", "Read", "Update", "Delete"
LOGIN, LOGOUT, LOGIN_FAILED = "Login", "Logout", "Login Failed"
ACTION_TYPES = [
    (CREATE, CREATE),
    (READ, READ),
    (UPDATE, UPDATE),
    (DELETE, DELETE),
    (LOGIN, LOGIN),
    (LOGOUT, LOGOUT),
    (LOGIN_FAILED, LOGIN_FAILED),
]

SUCCESS, FAILED = "Success", "Failed"
ACTION_STATUS = [(SUCCESS, SUCCESS), (FAILED, FAILED)]

class ActivityLog(models.Model):
    actor = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    action_type = models.CharField(choices=ACTION_TYPES, max_length=15)
    action_time = models.DateTimeField(auto_now_add=True, editable=False)
    execution_time = models.CharField(max_length=155, verbose_name="Execution time (s)", null=True, blank=True)
    remarks = models.TextField(blank=True, null=True)
    status = models.CharField(choices=ACTION_STATUS, max_length=7, default=SUCCESS)
    status_code = models.PositiveIntegerField(null=True, blank=True)
    response = models.TextField(null=True, blank=True)
    data = models.JSONField(default=dict)

    # for generic relations
    content_type = models.ForeignKey(
        ContentType, models.SET_NULL, blank=True, null=True
    )
    object_id = models.PositiveIntegerField(blank=True, null=True)
    content_object = GenericForeignKey()

    def __str__(self) -> str:
        return f"{self.action_type} by {self.actor} on {self.action_time}"