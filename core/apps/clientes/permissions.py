from rest_framework import permissions

class IsAdminOrStaff(permissions.BasePermission):

    def has_permission(self, request, view):
        return not request.user.groups.filter(name="Clientes").exists()