from rest_framework import permissions, viewsets

from ..models import Appointment
from ..permissions import IsOwnerOfSchedule
from ..serializers import AppointmentSerializer


class AppointmentViewSet(viewsets.ModelViewSet):
    permission_classes = (IsOwnerOfSchedule, permissions.IsAuthenticated)
    serializer_class = AppointmentSerializer

    def get_queryset(self):
        schedule = self.request.user.schedule  # type: ignore
        return Appointment.objects.filter(schedule=schedule)
