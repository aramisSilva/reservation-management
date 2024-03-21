from rest_framework import permissions

class IsClienteUser(permissions.BasePermission):
    """
    Permissão personalizada para permitir apenas aos clientes acessarem determinada view.
    """

    def has_permission(self, request, view):
        if request.user and request.user.groups.filter(name='Clientes').exists():
            return True
        return False