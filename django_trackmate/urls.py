from django.urls import include, path

from .views import trackmate_admin, fetch_logs

name="django_trackmate"
urlpatterns = [
    path('trackmate-admin/', trackmate_admin, name='trackmate_admin'),
    path("fetch-logs/", fetch_logs, name="fetch_logs")
]