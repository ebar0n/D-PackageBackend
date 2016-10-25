from django.contrib.auth.models import AbstractUser
from django.db import models


class ShipmentType(models.Model):
    name = models.CharField(verbose_name='Nombre', max_length=100)
    description = models.CharField(verbose_name='Descripción', max_length=100)
    codename = models.CharField(verbose_name='Codigo', max_length=100)
    icon = models.CharField(verbose_name='Icono', max_length=100)
    insured_value = models.DecimalField(verbose_name='Valor asegurado', max_digits=6, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        verbose_name = 'Tipo de envio'
        verbose_name_plural = 'Tipos de envios'


class Shipment(models.Model):
    client = models.ForeignKey('sw_users.ClientAccount', verbose_name='Cliente')
    service = models.ForeignKey('sw_users.ServiceAccount', verbose_name='Prestador de servicio', null=True)

    shipmenttype = models.ForeignKey('ShipmentType', verbose_name='Tipo de envio')
    packagetype = models.ForeignKey('sw_vehicles.PackageType', verbose_name='Tipo de paquete')
    photo1 = models.ImageField(verbose_name='Foto', upload_to='shipmentPhoto', blank=True)
    photo2 = models.ImageField(verbose_name='Foto', upload_to='shipmentPhoto', blank=True)
    photo3 = models.ImageField(verbose_name='Foto', upload_to='shipmentPhoto', blank=True)
    tags = models.CharField(verbose_name='Etiquetas', max_length=100)
    receiver = models.CharField(verbose_name='Receptor', max_length=100)
    origin = models.CharField(verbose_name='Origen', max_length=100)
    destination = models.CharField(verbose_name='Destino', max_length=100)
    insured_value = models.DecimalField(verbose_name='Valor asegurado', max_digits=6, decimal_places=2, default=0)
    price = models.DecimalField(verbose_name='Precio', max_digits=6, decimal_places=2, default=0)
    reputation = models.OneToOneField('Reputation', verbose_name='Reputation')

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        verbose_name = 'Envio'
        verbose_name_plural = 'Envios'


class Reputation(models.Model):
    
    commentary = models.CharField(verbose_name='Comentario', max_length=100)
    score = models.IntegerField(verbose_name='Puntuacion')

    class Meta:
        verbose_name = 'Reputación'
        verbose_name_plural = 'Reputacion'