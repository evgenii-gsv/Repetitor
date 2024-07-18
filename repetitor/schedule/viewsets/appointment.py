from rest_framework import viewsets, permissions

from ..serializers import AppointmentSerializer
from ..models import Appointment
from ..permissions import IsOwnerOfSchedule


class AppointmentViewSet(viewsets.ModelViewSet):
    permission_classes = (IsOwnerOfSchedule, permissions.IsAuthenticated)
    serializer_class = AppointmentSerializer

    def get_queryset(self):
        schedule = self.request.user.schedule  # type: ignore
        return Appointment.objects.filter(schedule=schedule)
