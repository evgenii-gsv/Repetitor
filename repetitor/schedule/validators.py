from rest_framework import serializers

from .models import Appointment


class StartBeforeEndValidator:
    """
    Validating that the start datetime is before end datetime
    """
    message = '{end_datetime_field} should be after {start_datetime_field}'

    def __init__(
        self,
        start_datetime_field: str = 'start',
        end_datetime_field: str = 'end',
        message: str | None = None,
        instance: serializers.ModelSerializer | None = None,
    ) -> None:
        self.start_datetime_field = start_datetime_field
        self.end_datetime_field = end_datetime_field
        self.message = message or self.message
        self.instance = instance

    def __call__(self, attrs: dict) -> None:
        start = attrs.get(self.start_datetime_field, self.instance.start if self.instance else None)  # type: ignore
        end = attrs.get(self.end_datetime_field, self.instance.end if self.instance else None)  # type: ignore

        if start >= end:
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
        self,
        schedule_id_field: str = 'schedule_id',
        start_datetime_field: str = 'start',
        end_datetime_field: str = 'end',
        message: str | None = None,
        instance: serializers.ModelSerializer | None = None,
    ) -> None:
        self.schedule_id_field = schedule_id_field
        self.start_datetime_field = start_datetime_field
        self.end_datetime_field = end_datetime_field
        self.message = message or self.message
        self.instance = instance

    def __call__(self, attrs: dict) -> None:
        queryset = Appointment.objects.filter(
            schedule_id=attrs.get(self.schedule_id_field,
                                  self.instance.schedule.pk if self.instance else None),  # type: ignore
            start__lt=attrs.get(self.end_datetime_field, self.instance.end if self.instance else None),  # type: ignore
            end__gt=attrs.get(self.start_datetime_field,
                              self.instance.start if self.instance else None)  # type: ignore
        )
        if self.instance:
            queryset = queryset.exclude(pk=self.instance.pk)  # type: ignore
        if appointment := queryset.first():
            message = self.message.format(appointment_id=appointment.pk,)
            raise serializers.ValidationError(message)
