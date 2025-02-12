from django.apps import AppConfig


class DjLoggerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'django_trackmate'
    label = 'django_trackmate'

    def ready(self):
        from . import signals
