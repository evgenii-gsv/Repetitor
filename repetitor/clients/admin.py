from django.contrib import admin

from .models import Client, Person, Group

admin.site.register(Client)
admin.site.register(Person)
admin.site.register(Group)
