from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """ Allow an user to edit her own profile"""

    def has_object_permission(self, request, view, obj):
        """Check if the user try to edit her own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id

class UpdateOwnStatus(permissions.BasePermission):
    """ Allow update from status feed"""    

    def has_object_permission(self, request, view, obj):
        """Check if the user try to edit her own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile_id == request.user.id