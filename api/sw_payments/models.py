from django.db import models

TYPE_ACCOUNT = [
    ['Ah', 'Ahorro'],
    ['Co', 'Corriente'],
]


class Bank(models.Model):

    name = models.CharField(verbose_name='Nombre', max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        verbose_name = 'Banco'
        verbose_name_plural = 'Bancos'


class BankAccount(models.Model):

    holder = models.CharField(verbose_name='Titular', max_length=100)
    identity_card = models.CharField(verbose_name='Cedula de identidad', max_length=8)
    number = models.CharField(verbose_name='Numero', max_length=20)
    type = models.CharField(verbose_name='Tipo', choices=TYPE_ACCOUNT, max_length=10)
    bank = models.ForeignKey('Bank', verbose_name='Banco')
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        verbose_name = 'Cuenta bancaria'
        verbose_name_plural = 'Cuentas bancarias'
