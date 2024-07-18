from django.conf import settings
from django.db import models
from django_extensions.db.models import TimeStampedModel


class Schedule(TimeStampedModel):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'Schedule of {self.user}'
