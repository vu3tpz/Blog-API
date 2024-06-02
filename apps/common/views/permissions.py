from rest_framework.permissions import BasePermission

from apps.access.models import Role


class CustomRolePermission(BasePermission):
    def has_permission(self, request, view):
        # Fetch the role associated with the user
        try:
            role = Role.objects.get(id=request.user.user_role)
        except:
            role = None

        if role:
            # Check if any of the associated permissions match the request method
            for permission in role.permission.all():
                method = permission.method
                allowed_methods = method
                if request.method in allowed_methods:
                    return True
            return False
        return False
