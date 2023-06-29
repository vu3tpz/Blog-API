from rest_framework.permissions import BasePermission

from .models import Role, RolePermission


class CustomRolePermission(BasePermission):
    def has_permission(self, request, view):
        # Fetch the role associated with the user
        role = Role.objects.get(name=request.user.role)

        # Fetch the permissions associated with the role
        permissions = RolePermission.objects.filter(role=role)

        # Check if any of the associated permissions match the request method
        for permission in permissions:
            methods = permission.objects.all()
            allowed_methods = [method.name for method in methods]
            if request.method in allowed_methods:
                return True
        return False
