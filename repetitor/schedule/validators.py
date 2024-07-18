from rest_framework import serializers


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
            raise serializers.ValidationError(
                {self.end_datetime_field: message}
            )
