from django.contrib import admin

from .models import Appointment, Schedule

admin.site.register(Schedule)
admin.site.register(Appointment)
