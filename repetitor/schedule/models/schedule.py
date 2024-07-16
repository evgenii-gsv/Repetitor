from django.db import models
from django.conf import settings
from django_extensions.db.models import TimeStampedModel


class Schedule(TimeStampedModel):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
