# coding=utf-8

import logging

import stripe
from django.conf import settings
from django.utils.translation import ugettext as _

stripe.api_key = settings.STRIPE_SECRET_KEY

STRIPE_ERROR_MSG = {
  'invalid_request_error': _('Invalid request error.'),
  'api_connection_error': _('Failure to connect to Stripe\'s API.'),
  'authentication_error': _('Failure to properly authenticate yourself in the request.'),
  'rate_limit_error': _('Too many requests hit the API too quickly.'),
  'card_error': _('Card can\'t be charged for some reason.'),
  'api_error': _('Temporary problem with Stripe\'s servers'),
  'incorrect_number': _('The card number is incorrect.'),
  'invalid_number': _('The card number is not a valid credit card number.'),
  'invalid_expiry_month': _('The card\'s expiration month is invalid.'),
  'invalid_expiry_year': _('The card\'s expiration year is invalid.'),
  'invalid_cvc': _('The card\'s security code is invalid.'),
  'expired_card': _('The card has expired.'),
  'incorrect_cvc': _('The card\'s security code is incorrect.'),
  'incorrect_zip': _('The card\'s zip code failed validation.'),
  'card_declined': _('The card was declined.')
}


def catch_stripe_exceptions(fun):
    """
        Decorator to catch stripe exceptions
    Args:
        fun:

    Returns:

    """
    stripe_logger = logging.getLogger('stripe')

    def inner(*args, **kwargs):
        try:
            result = fun(*args, **kwargs)
        except Exception as e:
            if hasattr(e, 'json_body'):
                stripe_logger.error(e.json_body)
                e.json_body['error']['original_message'] = e.json_body['error']['message']

                if 'code' in e.json_body['error']:
                    e.json_body['error']['message'] = STRIPE_ERROR_MSG.get(e.json_body['error']['code'])
                else:
                    e.json_body['error']['message'] = STRIPE_ERROR_MSG.get(e.json_body['error']['type'])

                return None, e.json_body
            else:
                error_msg = {
                    'error': {
                        'message': 'Error: {}'.format(e)
                    }
                }
                stripe_logger.error(error_msg)
                return None, error_msg
        else:
            return result

    return inner


@catch_stripe_exceptions
def get_customer(user, stripe_token=None, create_without_card=False):
    """

    Args:
        user: Account object
        stripe_token: str

    Returns:

    """
    if stripe_token is None:
        stripe_token = {}
    if getattr(user, 'stripe_customer'):
        customer = stripe.Customer.retrieve(user.stripe_customer)
        if stripe_token:
            card = customer.sources.create(source=stripe_token)
            customer.default_source = card.id
            customer.save()
    else:
        if stripe_token or create_without_card:
            customer = stripe.Customer.create(
                description=user.get_full_name(),
                email=user.email,
                source=stripe_token
            )
            user.stripe_customer = customer.id
            user.save()
        else:
            error_msg = {
                'error': {
                    'message': _('Wrong Stripe Token. Stripe Token can\'t be None.')
                }
            }
            return None, error_msg

    return customer, {}


@catch_stripe_exceptions
def invoice_item(customer, subscription, amount, description=''):
    """

    Args:
        customer: Customer Object
        subscription: Stripe subscription id
        amount: int
        description: str

    Returns:

    """
    invoice_item_object = stripe.InvoiceItem.create(
        customer=customer,
        amount=amount,
        currency='usd',
        description=description,
        subscription=subscription
    )
    return invoice_item_object, {}


@catch_stripe_exceptions
def invoice_pay(customer, subscription):
    """

    Args:
        customer: Customer Object
        subscription: Stripe subscription id

    Returns:

    """
    invoice_object = stripe.Invoice.create(
        customer=customer,
        subscription=subscription
    )
    invoice_object.pay()
    return stripe.Invoice.retrieve(invoice_object.id), {}


@catch_stripe_exceptions
def payment_history(customer, limit=20, starting_after=None):
    return stripe.Invoice.list(customer=customer, limit=limit, starting_after=starting_after), {}


@catch_stripe_exceptions
def card_create(user, stripe_token):
    customer, response_customer = get_customer(user=user, create_without_card=True)
    if not customer:
        return customer, response_customer

    card = customer.sources.create(source=stripe_token)
    customer.default_source = card.id
    customer.save()
    return card, {}


@catch_stripe_exceptions
def card_list(user, limit=20, starting_after=None):
    customer, response_customer = get_customer(user=user, create_without_card=True)
    if not customer:
        return customer, response_customer

    cards = customer.sources.all(object='card', limit=limit, starting_after=starting_after)
    return cards, {}


@catch_stripe_exceptions
def card_delete(user, card_id):
    customer, response_customer = get_customer(user=user, create_without_card=True)
    if not customer:
        return customer, response_customer

    customer.sources.retrieve(card_id).delete()
    return True, {}


@catch_stripe_exceptions
def card_default(user, card_id=None):
    customer, response_customer = get_customer(user=user, create_without_card=True)
    if not customer:
        return customer, response_customer
    if card_id:
        customer.default_source = card_id
        customer.save()
    return {'id': customer.default_source}, {}
