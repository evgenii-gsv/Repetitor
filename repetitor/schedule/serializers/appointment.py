from rest_framework import serializers

from ..models import Appointment
from ..validators import StartBeforeEndValidator


class AppointmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Appointment
        fields = ('id', 'start', 'end', 'price',)
        validators = [
            StartBeforeEndValidator(),
        ]
