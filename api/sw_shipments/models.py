from django.contrib.gis.db import models
from django.utils.translation import ugettext as _


class ShipmentType(models.Model):
    name = models.CharField(verbose_name=_('name'), max_length=100)
    description = models.TextField(verbose_name=_('description'), max_length=200)
    codename = models.CharField(verbose_name=_('codename'), max_length=100)
    icon = models.CharField(verbose_name=_('icon'), max_length=100)
    insured_value = models.DecimalField(verbose_name=_('insured value'), max_digits=6, decimal_places=2)
    price = models.DecimalField(verbose_name=_('price'), max_digits=6, decimal_places=2)
    created_at = models.DateTimeField(verbose_name=_('created at'), auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(verbose_name=_('updated at'), auto_now=True, editable=False)

    class Meta:
        verbose_name = _('shipment type')
        verbose_name_plural = _('shipment types')


class Shipment(models.Model):
    client = models.ForeignKey('sw_users.ClientAccount', verbose_name=_('client'))
    service = models.ForeignKey('sw_users.ServiceAccount', verbose_name=_('service provider'), null=True)
    shipmenttype = models.ForeignKey('ShipmentType', verbose_name=_('shipment type'))
    packagetype = models.ForeignKey('sw_vehicles.PackageType', verbose_name=_('package type'))
    photo1 = models.ImageField(verbose_name=_('photo 1'), upload_to='shipmentPhoto', blank=True)
    photo2 = models.ImageField(verbose_name=_('photo 2'), upload_to='shipmentPhoto', blank=True)
    photo3 = models.ImageField(verbose_name=_('photo 3'), upload_to='shipmentPhoto', blank=True)
    tags = models.CharField(verbose_name=_('tags'), max_length=100)
    receiver = models.CharField(verbose_name=_('receiver'), max_length=100)
    origin = models.PointField(verbose_name=_('origin'))
    destination = models.PointField(verbose_name=_('destination'))
    insured_value = models.DecimalField(verbose_name=_('insured value'), max_digits=6, decimal_places=2, default=0)
    price = models.DecimalField(verbose_name=_('price'), max_digits=6, decimal_places=2, default=0)
    reputation = models.OneToOneField('Reputation', verbose_name=_('reputation'))
    status = models.ForeignKey('Status', verbose_name=_('status'))
    created_at = models.DateTimeField(verbose_name=_('created at'), auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(verbose_name=_('updated at'), auto_now=True, editable=False)

    class Meta:
        verbose_name = _('shipment')
        verbose_name_plural = _('shipment')


class Reputation(models.Model):

    commentary = models.TextField(verbose_name=_('commentary'))
    score = models.PositiveSmallIntegerField(verbose_name=_('score'))
    created_at = models.DateTimeField(verbose_name=_('created at'), auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(verbose_name=_('updated at'), auto_now=True, editable=False)

    class Meta:
        verbose_name = 'Reputación'
        verbose_name_plural = 'Reputacion'


class Metric(models.Model):

    name = models.CharField(verbose_name=_('name'), max_length=100)
    value = models.DecimalField(verbose_name=_('value'), max_digits=6, decimal_places=2)
    created_at = models.DateTimeField(verbose_name=_('created at'), auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(verbose_name=_('updated at'), auto_now=True, editable=False)

    class Meta:
        verbose_name = _('metric')
        verbose_name_plural = _('metrics')


class Status(models.Model):

    name = models.CharField(verbose_name=_('name'), max_length=100)
    codename = models.CharField(verbose_name=_('codename'), max_length=100)
    created_at = models.DateTimeField(verbose_name=_('created at'), auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(verbose_name=_('updated at'), auto_now=True, editable=False)

    class Meta:
        verbose_name = _('status')
        verbose_name_plural = _('status')
