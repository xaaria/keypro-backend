from rest_framework import permissions

class IsPOIOwner(permissions.BasePermission):

    message = 'Only allowed for own items'

    def has_object_permission(self, request, view, obj):
        return obj.created_by == request.auth.user