# -*- coding: utf-8 -*-
from rest_framework import permissions


class IsAdminOrAccountOwner(permissions.BasePermission):
    """
    Returns true if the request.user is owner of the account or Admin

    """

    def has_object_permission(self, request, view, account):
        """
        Return `True` if permission is granted, `False` otherwise.

        :return: bool
        """
        if request.user.is_authenticated():
            if request.user.is_staff:
                return True
            return account.username == request.user.username
        return False


class IsClientAccountOwner(permissions.BasePermission):
    """
    Returns true if the request.user is owner of the account or Admin

    """

    def has_object_permission(self, request, view, account):
        """
        Return `True` if permission is granted, `False` otherwise.

        :return: bool
        """
        if request.user.is_authenticated():
            if request.user.client:
                return True
            return False
        return False


class IsServiceAccountOwner(permissions.BasePermission):
    """
    Returns true if the request.user is owner of the account or Admin

    """

    def has_object_permission(self, request, view, account):
        """
        Return `True` if permission is granted, `False` otherwise.

        :return: bool
        """
        if request.user.is_authenticated():
            if request.user.service:
                return True
            return False
        return False
