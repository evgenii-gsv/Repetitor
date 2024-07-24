from rest_framework import routers

from .viewsets import AppointmentViewSet

router = routers.SimpleRouter()
router.register('', AppointmentViewSet, basename='appointment')

urlpatterns = router.urls
