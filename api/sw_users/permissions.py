# -*- coding: utf-8 -*-
from rest_framework import permissions
from sw_users import models


class IsAdminOrAccountOwner(permissions.BasePermission):
    """
    Returns true if the request.user is owner of the account or Admin

    """

    def has_object_permission(self, request, view, obj):
        """
        Return `True` if permission is granted, `False` otherwise.

        :return: bool
        """
        if request.user.is_authenticated():
            if request.user.is_staff:
                return True

            if type(obj) == models.ClientAccount:
                return request.user.client_id and request.user.pk == obj.useraccount.pk
            elif type(obj) == models.ServiceAccount:
                return request.user.service_id and request.user.pk == obj.useraccount.pk
            else:
                # Type(obj) is UserAccount
                return request.user.pk == obj.pk
        return False
