from rest_framework import serializers

from .models import Appointment


class StartBeforeEndValidator:
    """
    Validating that the start datetime is before end datetime
    """
    message = '{end_datetime_field} should be after {start_datetime_field}'

    def __init__(self, start_datetime_field='start', end_datetime_field='end', message=None):
        self.start_datetime_field = start_datetime_field
        self.end_datetime_field = end_datetime_field
        self.message = message or self.message

    def __call__(self, attrs):
        if attrs[self.start_datetime_field] >= attrs[self.end_datetime_field]:
            message = self.message.format(
                start_datetime_field=self.start_datetime_field,
                end_datetime_field=self.end_datetime_field,
            )
            raise serializers.ValidationError({self.end_datetime_field: message})


class EmptyWindowValidator:
    """
    Validating that there are no other appointments in this time period
    """
    message = 'This time window is blocked by appointment with id {appointment_id}.'

    def __init__(
        self, schedule_id_field='schedule_id', start_datetime_field='start', end_datetime_field='end', message=None
    ):
        self.schedule_id_field = schedule_id_field
        self.start_datetime_field = start_datetime_field
        self.end_datetime_field = end_datetime_field
        self.message = message or self.message

    def __call__(self, attrs):
        queryset = Appointment.objects.filter(
            schedule_id=attrs[self.schedule_id_field],
            start__lt=attrs[self.end_datetime_field],
            end__gt=attrs[self.start_datetime_field]
        )
        if appointment := queryset.first():
            message = self.message.format(appointment_id=appointment.pk,)
            raise serializers.ValidationError(message)
