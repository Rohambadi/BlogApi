from rest_framework import  permissions

SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')
class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):


        if request.method in permissions.SAFE_METHODS or request.user.is_superuser:
            return bool(request.user and request.user.is_authenticated)

        return obj.author == request.user

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS and
            request.user.is_authenticated or
            request.user and
            request.user.is_staff
        )








