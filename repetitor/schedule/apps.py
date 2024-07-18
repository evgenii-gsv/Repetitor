from django.apps import AppConfig


class ScheduleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'repetitor.schedule'

    def ready(self) -> None:
        from . import signals  # noqa: F401
