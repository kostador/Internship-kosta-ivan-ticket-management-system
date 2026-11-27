from django.contrib.auth.base_user import AbstractBaseUser
from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdmin(BasePermission):
    """"
    Allows access only to users with the ADMIN role.
    """
    def has_permission(self,request,view):
        return (request.user
            and request.user.is_authenticated
            and request.user.role == "ADMIN"
        )

class IsEmployee(BasePermission):
    """"
    Allows access only to users with the EMPLOYEE role.
    """

    def has_permission(self,request,view):
        return (
                request.user
                and request.user.is_authenticated
                and request.user.role == "EMPLOYEE"
        )



class IsAdminOrEmployee(BasePermission):
    """"
    Allows access only to authenticated Admin and Employee users.
    """

    def has_permission(self,request,view):
        return (
            request.user
            and request.user.is_authenticated
            and request.user.role in  ["EMPLOYEE","ADMIN"]
        )


class IsAdminOrReadOnly(BasePermission):
    """"
    Admin can perform all operations.
    Employees can only read data.
    """

    def has_permission(self,request,view):
        if not request.user or not request.user.is_authenticated:
            return False

        if request.user.role == "ADMIN":
            return True

        return (
            request.user.role == "EMPLOYEE"
            and request.method in SAFE_METHODS
        )

class IsAdminOrAssignedEmployee(BasePermission):
    """"
    Admin can access all tickets.
    Employees can only read tickets assigned to them.
    """

    def has_permission(self,request,view):
        return (
            request.user
            and request.user.is_authenticated
            and request.user.role in ["EMPLOYEE","ADMIN"]
        )

    def has_object_permission(self, request, view, obj):
        if request.user.role == "ADMIN":
            return True

        return (
            request.user.role == "EMPLOYEE"
            and request.method in SAFE_METHODS
            and obj.assignee_id == request.user.id
        )
