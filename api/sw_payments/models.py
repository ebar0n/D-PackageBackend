from django.contrib.gis.db import models
from django.utils.translation import ugettext as _

TYPE_ACCOUNT = [
    [1, _('Saving')],
    [2, _('Common')],
]


class Bank(models.Model):

    name = models.CharField(verbose_name=_('name'), max_length=100)
    created_at = models.DateTimeField(verbose_name=_('created at'), auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(verbose_name=_('updated at'), auto_now=True, editable=False)

    class Meta:
        verbose_name = _('bank')
        verbose_name_plural = _('banks')


class BankAccount(models.Model):

    holder = models.CharField(verbose_name=_('holder'), max_length=100)
    identity_card = models.CharField(verbose_name=_('identity card'), max_length=8)
    number = models.CharField(verbose_name=_('number'), max_length=20)
    type = models.IntegerField(verbose_name=_('type'), choices=TYPE_ACCOUNT)
    bank = models.ForeignKey('Bank', verbose_name=_('bank'))
    created_at = models.DateTimeField(verbose_name=_('created at'), auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(verbose_name=_('updated at'), auto_now=True, editable=False)

    class Meta:
        verbose_name = _('bank account')
        verbose_name_plural = _('bank accounts')
