from rest_framework import permissions

class IsPurchaserOrReadOnly(permissions.BasePermission):
  def has_object_permission(self, request, view, obj):
    #READ only permissions
    if request.method in permissions.SAFE_METHODS:
      return True
    
    return obj.item_purchaser == request.user