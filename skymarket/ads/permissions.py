from rest_framework import permissions

from users.models import UserRoles


class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.author or request.user.role == UserRoles.ADMIN
