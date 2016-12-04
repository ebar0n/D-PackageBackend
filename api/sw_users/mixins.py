# -*- coding: utf-8 -*-
from rest_framework import permissions
from sw_users.permissions import IsAdminOrAccountOwner, IsClientAccountOwner, IsServiceAccountOwner


class DefaultCRUDPermissions(object):
    """
    Mixin to verify if the user can access to a method through a web service

    """

    def get_permissions(self):
        """
        Get permissions

        """
        if self.action == 'create':
            return [permissions.AllowAny()]

        if self.action in ['update', 'partial_update', 'destroy', 'retrieve']:
            return [IsAdminOrAccountOwner()]

        if self.action == 'list':
            return [permissions.IsAdminUser()]

        return [permission() for permission in self.permission_classes]


class ClientCRUDPermissions(object):
    """
    Mixin to verify if the user can access to a method through a web service
    """

    def get_permissions(self):
        """
        Get permissions
        """
        if self.action == 'create':
            return [IsClientAccountOwner()]

        if self.action in ['update', 'partial_update', 'destroy', 'retrieve']:
            return [IsClientAccountOwner()]

        if self.action == 'list':
            return [IsClientAccountOwner]

        return [permission() for permission in self.permission_classes]


class ServiceCRUDPermissions(object):
    """
    Mixin to verify if the user can access to a method through a web service
    """

    def get_permissions(self):
        """
        Get permissions
        """
        if self.action == 'create':
            return [IsServiceAccountOwner()]

        if self.action in ['update', 'partial_update', 'destroy', 'retrieve']:
            return [IsServiceAccountOwner()]

        if self.action == 'list':
            return [IsServiceAccountOwner]

        return [permission() for permission in self.permission_classes]
