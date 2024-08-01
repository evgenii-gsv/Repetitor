from django.db import models
from django.urls import reverse
from django_extensions.db.models import TimeStampedModel

from .schedule import Schedule


class Appointment(TimeStampedModel):
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE, related_name='appointments')
    start = models.DateTimeField()
    end = models.DateTimeField()
    price = models.DecimalField(max_digits=19, decimal_places=2, default=0.0)  # type: ignore

    @property
    def duration(self):
        delta = self.start - self.end
        return (delta.days * 24 * 3600 + delta.seconds) // 60
    
    def get_absolute_url(self):
        return reverse('appointment-detail', kwargs={'pk': self.pk})
