# -*- coding: utf-8 -*-
from corporations.models import Corporation
from django.conf import settings
from django.db.models import Q
from django.http import Http404
from django.utils.translation import ugettext as _


class Domains(object):
    """
    Domains utils
    """

    @staticmethod
    def get_api(request):
        """
        Get domain ip

        :param request: request object
        :return: domain

        """
        return 'http{}://{}/'.format(
            's' if settings.SESSION_COOKIE_SECURE else '',
            request.META.get('HTTP_HOST', '')
        )

    @staticmethod
    def get_corporation(request):
        """
        Get corporation

        :param request: request object
        :return: Corporation object

        """
        try:
            domain = Domains.get_api(request)
            return Corporation.objects.get(
                Q(domain_api=domain) | Q(domain_app=domain)
            )
        except Corporation.DoesNotExist:
            raise Http404(_('No {} matches the given query.').format(Corporation._meta.object_name))
