from rest_framework import permissions


class IsOwnerOrManager(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(request.user and request.user.is_authenticated and request.user == obj)


class IsOwnerOrManagerOrCreateOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return True
        return bool(request.user and request.user.is_authenticated and request.user.role in ['owner', 'manager'])