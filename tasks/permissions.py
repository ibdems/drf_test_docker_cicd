from rest_framework.permissions import BasePermission


class IsCompletedAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        return not obj.completed

    def has_permission(self, request, view):
        return request.user.is_superuser


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method == "DELETE":
            return request.user.is_superuser
        return True
