from django.db import models
from django_extensions.db.models import TimeStampedModel
from django.conf import settings

from repetitor.balance.models import Balance


class Person(TimeStampedModel):
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='person_clients')
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    notes = models.TextField()
    balance = models.OneToOneField(Balance, on_delete=models.CASCADE)
