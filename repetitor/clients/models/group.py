from django.db import models
from django_extensions.db.models import TimeStampedModel
from django.conf import settings

from repetitor.balance.models import Balance
from .person import Person


class Group(TimeStampedModel):
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='group_clients')
    name = models.CharField(max_length=100)
    people = models.ManyToManyField(Person, blank=True, null=True, related_name='groups')
    notes = models.TextField(blank=True, null=True)
    # balance = models.OneToOneField(Balance, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'Group: {self.name}'
