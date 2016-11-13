from django.db import models
from colorful.fields import RGBColorField
from django.contrib.postgres.fields import IntegerRangeField


class PackageType(models.Model):

    name = models.CharField(verbose_name='Nombre', max_length=100)
    description = models.CharField(verbose_name='Descripción', max_length=100)
    codename = models.CharField(verbose_name='Codigo', max_length=100)
    weight = IntegerRangeField(verbose_name='Peso')
    height = IntegerRangeField(verbose_name='Altura')
    width = IntegerRangeField(verbose_name='Anchura')
    price = models.DecimalField(verbose_name='Precio', max_digits=6, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        verbose_name = 'Tipo de paquete'
        verbose_name_plural = 'Tipos de paquetes'


class VehicleCategory(models.Model):

    name = models.CharField(verbose_name='Nombre', max_length=100)
    description = models.TextField(verbose_name='Descripción', max_length=200)
    codename = models.CharField(verbose_name='Codigo', max_length=100)
    icon = models.CharField(verbose_name='Icono', max_length=100)
    packagetype = models.ManyToManyField('PackageType', verbose_name='Tipos de paquete', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        verbose_name = 'Categoria de vehiculo'
        verbose_name_plural = 'Categorias de vehiculo'


class Model(models.Model):

    name = models.CharField(verbose_name='Nombre', max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        verbose_name = 'Modelo de vehiculo'
        verbose_name_plural = 'Modelo de vehiculo'


class Vehicle(models.Model):

    license_plate = models.CharField(verbose_name='Nombre', max_length=100)
    model = models.ForeignKey('Model', verbose_name='Modelo')
    category = models.ForeignKey('VehicleCategory', verbose_name='Categoria')
    color = RGBColorField()
    photo1 = models.ImageField(verbose_name='Foto', upload_to='vehiculePhoto', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        verbose_name = 'Vehiculo'
        verbose_name_plural = 'Vehiculos'
