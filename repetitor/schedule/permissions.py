from rest_framework import permissions


class IsOwnerOfSchedule(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.schedule == request.user.schedule
