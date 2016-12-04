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
            return request.user.pk == account.pk
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
            if request.user.client_id and request.user.pk == account.pk:
                return True
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
            if request.user.service_id and request.user.pk == account.pk:
                return True
        return False
