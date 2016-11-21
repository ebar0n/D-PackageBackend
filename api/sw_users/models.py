import uuid

from django.contrib.auth.models import AbstractUser
from django.contrib.gis.db import models
from django.utils.translation import ugettext as _


class UserAccount(AbstractUser):
    """
    UserAccount: Cuentas de usuario
    Modelo que gestiona los usuarios para las cuentas.
    **Atributos db:**
        - ... Atributos heredados desde AbstractUser: username, first_name,
          last_name, email, is_staff, is_active, date_join.
          Desde AbstracBaseUser: password, last_login.
          Desde PermissionsMixin: is_superuser, groups, user_permissions.
        - check_mail (BooleanField): Booleano que registra si la cuenta tiene
          el correo verificado.
        - token (UUIDField): Token para validaciones unicas.
        - token_expires (DateTimeField): Fecha de expiracion para el token.
    """
    client = models.OneToOneField(
        'ClientAccount',
        verbose_name=_('client'),
        null=True, editable=False
    )
    service = models.OneToOneField(
        'ServiceAccount',
        verbose_name=_('service provider'),
        null=True, editable=False
    )
    check_mail = models.BooleanField(verbose_name=_('check mail'), default=False)
    stripe_customer = models.CharField(verbose_name=_('stripe, customer ID'), max_length=64, blank=True)
    token = models.UUIDField(default=uuid.uuid4, editable=False)
    token_expires = models.DateTimeField(null=True, editable=False)

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_account(self):
        if self.client_id:
            return self.client
        elif self.service_id:
            return self.service


class ClientAccount(models.Model):
    """
    ClientAccount: Cuenta para clientes
    Se gestionan las cuentas de clientes existentes en el sistema.
    **Atributos db:**
        - phone (CharField): Número telefónico.
        - created_at (DateTimeField): Fecha de creación del registro
        - updated_at (DateTimeField): Fecha de actualización del registro
    """

    phone = models.CharField(verbose_name=_('phone'), max_length=11)
    created_at = models.DateTimeField(verbose_name=_('created at'), auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(verbose_name=_('updated at'), auto_now=True, editable=False)

    class Meta:
        verbose_name = _('client')
        verbose_name_plural = _('clients')


class ServiceAccount(models.Model):
    """
    ServiceAccount: Cuenta para prestadores de servicio
    **Atributos db:**
    """
    identity_card = models.CharField(verbose_name='Cedula de identidad', max_length=8)
    driver_license = models.CharField(verbose_name='Licencia de conducir', max_length=20)
    phone = models.CharField(verbose_name='Telefóno', max_length=11)
    photo = models.ImageField(verbose_name='Foto', upload_to='servicePhoto', blank=True)
    birthdate = models.DateField(verbose_name='Fecha de nacimiento')
    address = models.CharField(verbose_name='Dirección', max_length=100)
    vehicle = models.OneToOneField('sw_vehicles.Vehicle', verbose_name='Vehículo')
    identity_check = models.BooleanField(verbose_name='Identidad verificada', default=False)
    bankaccount = models.OneToOneField('sw_payments.BankAccount', verbose_name='Cuenta bancaria', null=True)
    balance = models.DecimalField(verbose_name='Saldo', max_digits=6, decimal_places=4, default=0)
    last_location_point = models.PointField(verbose_name=_('last location point'), null=True, blank=True)
    last_location_date = models.DateTimeField(verbose_name=_('last location date'), blank=True, null=True)
    created_at = models.DateTimeField(verbose_name=_('created at'), auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(verbose_name=_('updated at'), auto_now=True, editable=False)

    class Meta:
        verbose_name = _('service provider')
        verbose_name_plural = _('services provider')
