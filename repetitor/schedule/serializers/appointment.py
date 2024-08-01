from rest_framework import serializers

from ..models import Appointment
from ..validators import EmptyWindowValidator, StartBeforeEndValidator

import logging


logger = logging.getLogger()


class CurrentScheduleIdDefault:
    requires_context = True

    def __call__(self, serializer_field) -> int:
        return serializer_field.context['request'].user.schedule.pk

    def __repr__(self):
        return '%s()' % self.__class__.__name__


class AppointmentSerializer(serializers.ModelSerializer):

    schedule_id = serializers.HiddenField(default=CurrentScheduleIdDefault())

    def get_validators(self):
        return [
            StartBeforeEndValidator(instance=self.instance), 
            EmptyWindowValidator(instance=self.instance)
            ]

    class Meta:
        model = Appointment
        fields = (
            'id',
            'start',
            'end',
            'price',
            'schedule_id',
        )
