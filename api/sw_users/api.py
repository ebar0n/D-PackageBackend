import datetime
import uuid

from django.contrib.auth import authenticate, login, logout
from django.utils import timezone
from django.utils.translation import ugettext as _
from rest_framework import permissions, status, views, viewsets
from rest_framework.authtoken.models import Token
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
from sw_users import mixins
from sw_users.models import ClientAccount, ServiceAccount, UserAccount
from sw_users.permissions import IsAdminOrAccountOwner
from sw_users.serializers import (
    ChangePasswordSerializer, ClientAccountSerializer, ForgotPasswordSerializer, LoginSerializer,
    ResetPasswordChangeSerializer, ServiceAccountSerializer, UserAccountSerializer,
)
from utils.tasks.emails import send_mail


class ClientAccountViewSet(mixins.DefaultCRUDPermissions, viewsets.ModelViewSet):
    lookup_field = 'useraccount__username'
    queryset = ClientAccount.objects.all()
    serializer_class = ClientAccountSerializer


class ServiceAccountViewSet(mixins.DefaultCRUDPermissions, viewsets.ModelViewSet):
    lookup_field = 'useraccount__username'
    queryset = ServiceAccount.objects.all()
    serializer_class = ServiceAccountSerializer


class LoginView(views.APIView):
    """
    Login View
    """
    serializer_class = LoginSerializer

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
                token = Token.objects.create(user=user)
                if user.client:
                    serialized_account = ClientAccountSerializer(user.client)
                else:
                    serialized_account = ServiceAccountSerializer(user.service)
                data = serialized_account.data
                data['token'] = token.key
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
        logout(request)
        return Response({}, status=status.HTTP_204_NO_CONTENT)


class UserAccountViewSet(mixins.DefaultCRUDPermissions, viewsets.ReadOnlyModelViewSet):
    queryset = UserAccount.objects.all()
    serializer_class = UserAccountSerializer

    @list_route(methods=['post'], permission_classes=[permissions.AllowAny])
    def forgot_password(self, request, *args, **kwargs):
        serializer = ForgotPasswordSerializer(
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

        if user.token_expires and user.token_expires > timezone.now():
            return Response({
                'status': 'Bad request',
                'message': _('We already sent a link to reset the password.')
            }, status.HTTP_400_BAD_REQUEST)

        user.token = uuid.uuid4()
        user.token_expires = timezone.now() + datetime.timedelta(hours=4)
        user.save(update_fields=['token', 'token_expires'])

        url = '{}/api/v1/user/reset_password/{}/{}'.format(
            request.META['HTTP_HOST'],
            user.email,
            user.token.hex
        )
        data = {
            'name': user.get_full_name(),
            'url': url,
        }
        send_mail.run([user.email], _('Reset password'), 'reset_password.html', data)

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    @list_route(methods=['post'], permission_classes=[permissions.AllowAny])
    def reset_password(self, request, *args, **kwargs):
        serializer = ResetPasswordChangeSerializer(
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
        user.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    @detail_route(methods=['post'], permission_classes=[IsAdminOrAccountOwner])
    def change_password(self, request, *args, **kwargs):
        """
        Change the password of the account

        """
        user = self.get_object()
        serializer = ChangePasswordSerializer(
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

        return Response({}, status.HTTP_204_NO_CONTENT)
