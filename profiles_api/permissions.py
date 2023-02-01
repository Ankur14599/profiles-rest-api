from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Used for updating basic details"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.id == request.user.id

class UpdateOwnStatus(permissions.BasePermission):
    """Used for updating status in feed"""

    def has_object_permission(self, request, view, obj):
        """User is trying to update their own status"""
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user_profile.id == request.user.id
