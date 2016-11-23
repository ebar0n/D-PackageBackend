from colorful.fields import RGBColorField
from django.contrib.gis.db import models
from django.contrib.postgres.fields import IntegerRangeField
from django.utils.translation import ugettext as _
from django.core.validators import RegexValidator
plate_validator = RegexValidator(r'^.{7}$', "El numero de placa debe ser de 7 caracteres")


class PackageType(models.Model):

    name = models.CharField(verbose_name=_('name'), max_length=100, unique=True)
    description = models.TextField(verbose_name=_('description'), max_length=200)
    codename = models.CharField(verbose_name=_('codename'), max_length=100, unique=True)
    weight = IntegerRangeField(verbose_name=_('weight'))
    height = IntegerRangeField(verbose_name=_('height'))
    width = IntegerRangeField(verbose_name=_('width'))
    price = models.DecimalField(verbose_name=_('price'), max_digits=6, decimal_places=2)
    created_at = models.DateTimeField(verbose_name=_('created at'), auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(verbose_name=_('updated at'), auto_now=True, editable=False)

    class Meta:
        verbose_name = _('package type')
        verbose_name_plural = _('package types')

    def __str__(self):
        return self.name


class VehicleCategory(models.Model):

    name = models.CharField(verbose_name=_('name'), max_length=100, unique=True)
    description = models.TextField(verbose_name=_('description'), max_length=200)
    codename = models.CharField(verbose_name=_('codename'), max_length=100, unique=True)
    icon = models.CharField(verbose_name=_('icon'), max_length=100)
    packagetype = models.ManyToManyField('PackageType', verbose_name=_('package type'), blank=True)
    created_at = models.DateTimeField(verbose_name=_('created at'), auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(verbose_name=_('updated at'), auto_now=True, editable=False)

    class Meta:
        verbose_name = _('vehicle category')
        verbose_name_plural = _('vehicle categories')

    def __str__(self):
        return self.name


class Model(models.Model):

    name = models.CharField(verbose_name=_('name'), max_length=100)
    created_at = models.DateTimeField(verbose_name=_('created at'), auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(verbose_name=_('updated at'), auto_now=True, editable=False)

    class Meta:
        verbose_name = _('vehicle model')
        verbose_name_plural = _('vehicle models')

    def __str__(self):
        return self.name


class Vehicle(models.Model):

    license_plate = models.CharField(verbose_name=_('license plate'), max_length=7, validators=[plate_validator])
    model = models.ForeignKey('Model', verbose_name=_('model'))
    category = models.ForeignKey('VehicleCategory', verbose_name=_('category'))
    color = RGBColorField()
    photo1 = models.ImageField(verbose_name=_('photo 1'), upload_to='vehiculePhoto', blank=True)
    created_at = models.DateTimeField(verbose_name=_('created at'), auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(verbose_name=_('updated at'), auto_now=True, editable=False)

    class Meta:
        verbose_name = _('vehicle')
        verbose_name_plural = _('vehicles')

    def __str__(self):
        return self.license_plate
