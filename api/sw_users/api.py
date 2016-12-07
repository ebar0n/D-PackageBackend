import datetime
import uuid

from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from django.utils.translation import ugettext as _
from rest_framework import permissions, status, views, viewsets
from rest_framework.authtoken.models import Token
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
from sw_users import mixins, serializers, stripe
from sw_users.models import ClientAccount, ServiceAccount, UserAccount
from sw_users.permissions import IsAdminOrAccountOwner
from utils.tasks.emails import send_mail


class ClientAccountViewSet(mixins.DefaultCRUDPermissions, viewsets.ModelViewSet):
    lookup_field = 'useraccount__id'
    queryset = ClientAccount.objects.all()
    serializer_class = serializers.ClientAccountSerializer


class ServiceAccountViewSet(mixins.DefaultCRUDPermissions, viewsets.ModelViewSet):
    lookup_field = 'useraccount__id'
    queryset = ServiceAccount.objects.all()
    serializer_class = serializers.ServiceAccountSerializer


class LoginView(views.APIView):
    """
    Login View
    """
    serializer_class = serializers.LoginSerializer

    def post(self, request, format=None):
        """
        Authenticate the user
        """

        serializer = self.serializer_class(data=request.data)

        if not serializer.is_valid():
            return Response({'errors': serializer.errors}, status.HTTP_400_BAD_REQUEST)

        data = serializer.data
        username = data.get('username')
        password = data.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                token = Token.objects.get_or_create(user=user)
                if user.client:
                    serialized_account = serializers.ClientAccountSerializer(user.client)
                    _type = 'client'
                elif user.service:
                    serialized_account = serializers.ServiceAccountSerializer(user.service)
                    _type = 'service'
                else:
                    serialized_account = serializers.UserAccountSerializer(user)
                    _type = 'admin'
                data = serialized_account.data
                data['token'] = token[0].key
                data['type'] = _type
                return Response(data)
            else:
                return Response({
                    'status': 'Unauthorized',
                    'message': _('You need to activate your account first. '
                                'An email was sent to your inbox with the activation link')
                }, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({
                'status': 'Unauthorized',
                'message': _('Username/password combination invalid.')
            }, status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(views.APIView):
    """
    Logout View
    """
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        """
        Unauthenticated the user
        """
        try:
            request.user.auth_token.delete()
        except ObjectDoesNotExist:
            logout(request)

        return Response({}, status=status.HTTP_204_NO_CONTENT)


class UserAccountViewSet(mixins.DefaultCRUDPermissions, viewsets.ModelViewSet):
    queryset = UserAccount.objects.all()
    serializer_class = serializers.UserAccountSerializer

    @list_route(methods=['post'], permission_classes=[permissions.AllowAny])
    def forgot_password(self, request, *args, **kwargs):
        serializer = serializers.ForgotPasswordSerializer(
            data=request.data
        )
        if not serializer.is_valid():
            return Response({'errors': serializer.errors}, status.HTTP_400_BAD_REQUEST)

        data = serializer.data
        try:
            user = UserAccount.objects.get(
                email=data.get('email').lower()
            )
            user.token = None
            user.token_expires = None
            user.save(update_fields=['token', 'token_expires'])

        except UserAccount.DoesNotExist:
            return Response({
                'status': 'Not Found',
                'message': _('User does not exist.')
            }, status.HTTP_404_NOT_FOUND)

        if user.token_expires and user.token_expires > timezone.now():
            return Response({
                'status': 'Bad request',
                'message': _('We already sent a link to reset the password.')
            }, status.HTTP_400_BAD_REQUEST)

        user.token = uuid.uuid4()
        user.token_expires = timezone.now() + datetime.timedelta(hours=4)
        user.save(update_fields=['token', 'token_expires'])

        url = '{}/api/v1/user/reset_password/{}/{}'.format(
            request.META.get('HTTP_HOST', ''),
            user.email,
            user.token.hex
        )
        data = {
            'name': user.get_full_name(),
            'url': url,
        }
        send_mail.delay([user.email], _('Reset password'), 'reset_password.html', data)

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    @list_route(methods=['post'], permission_classes=[permissions.AllowAny])
    def reset_password(self, request, *args, **kwargs):
        serializer = serializers.ResetPasswordChangeSerializer(
            data=request.data
        )
        if not serializer.is_valid():
            return Response({'errors': serializer.errors}, status.HTTP_400_BAD_REQUEST)

        data = serializer.data
        try:
            user = UserAccount.objects.get(
                email=data.get('email').lower()
            )
        except UserAccount.DoesNotExist:
            return Response({
                'status': 'Not Found',
                'message': _('User does not exist.')
            }, status.HTTP_404_NOT_FOUND)

        if user.token.hex != data.get('token'):
            return Response({
                'status': 'Bad request',
                'message': _('Token does not match with the user.')
            }, status.HTTP_400_BAD_REQUEST)

        if user.token_expires and user.token_expires < timezone.now():
            return Response({
                'status': 'Bad request',
                'message': _('The token has already expired, please request a new one.')
            }, status.HTTP_400_BAD_REQUEST)

        user.set_password(data.get('password'))
        user.token_expires = None
        user.token = None
        user.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    @detail_route(methods=['post'], permission_classes=[IsAdminOrAccountOwner])
    def change_password(self, request, *args, **kwargs):
        """
        Change the password of the account

        """
        user = self.get_object()
        serializer = serializers.ChangePasswordSerializer(
            data=request.data
        )
        if not serializer.is_valid():
            return Response({'errors': serializer.errors}, status.HTTP_400_BAD_REQUEST)

        data = serializer.data
        if not user.check_password(data.get('old_password')):
            return Response({
                'status': 'Bad request',
                'message': _('Current password does not match.')
            }, status=status.HTTP_400_BAD_REQUEST)

        user.set_password(data.get('new_password'))
        user.save(update_fields=['password'])

        # Force authentication with new credentials
        login(request, user)
        return Response({}, status.HTTP_204_NO_CONTENT)


class CardViewSet(viewsets.ViewSet):

    serializer_class = serializers.CardSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        user = request.user
        data = request.data
        serializer_in = serializers.CardCreateSerializer(data=data)
        if serializer_in.is_valid():
            card, response_message = stripe.card_create(user, serializer_in.data.get('stripe_token'))
            if card:
                serializer_out = self.serializer_class(card)
                return Response(serializer_out.data, status=status.HTTP_201_CREATED)
            else:
                return Response(response_message, status=status.HTTP_502_BAD_GATEWAY)
        else:
            return Response(serializer_in.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        user = request.user
        data = request.GET
        cards, response_message = stripe.card_list(
            user=user, starting_after=data.get('starting_after', None)
        )
        if cards:
            default, response_message = stripe.card_default(
                user=user, card_id=None
            )
            if default:
                serializer_list = self.serializer_class(cards.get('data', []), many=True)
                serializer_default = serializers.CardDefaultSerializer(default)
                data = {
                    'cards': serializer_list.data,
                    'card_default': serializer_default.data
                }
                return Response(data, status=status.HTTP_200_OK)
            else:
                return Response(response_message, status=status.HTTP_502_BAD_GATEWAY)
        else:
            return Response(response_message, status=status.HTTP_502_BAD_GATEWAY)

    def destroy(self, request, pk=None):
        user = request.user
        success, response_message = stripe.card_delete(
            user=user, card_id=pk
        )
        if success:
            return Response({}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(response_message, status=status.HTTP_502_BAD_GATEWAY)

    def update(self, request, pk):
        user = request.user
        card, response_message = stripe.card_default(
            user=user, card_id=pk
        )
        if card:
            serializer = serializers.CardDefaultSerializer(card)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(response_message, status=status.HTTP_502_BAD_GATEWAY)

    @list_route(methods=['GET'])
    def default(self, request):
        user = request.user
        card, response_message = stripe.card_default(
            user=user, card_id=None
        )
        if card:
            serializer = serializers.CardDefaultSerializer(card)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(response_message, status=status.HTTP_502_BAD_GATEWAY)
