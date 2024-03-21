from rest_framework import permissions


class IsAdminOrStaff(permissions.BasePermission):

    def has_permission(self, request, view):
        return not request.user.groups.filter(name="clientes").exists()


class IsAdminUser(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        return request.user.groups.filter(name='administradores').exists()


class IsSuperUser(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user and request.user.is_superuser
