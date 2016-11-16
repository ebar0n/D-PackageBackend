from django.contrib.auth import authenticate, login, logout
from rest_framework import permissions, status, views, viewsets
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from .models import ClientAccount, ServiceAccount
from .serializers import ClientAccountSerializer, LoginSerializer, ServiceAccountSerializer


class ClientAccountViewSet(viewsets.ModelViewSet):
    lookup_field = 'useraccount__username'
    queryset = ClientAccount.objects.all()
    serializer_class = ClientAccountSerializer


class ServiceAccountViewSet(viewsets.ModelViewSet):
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
                    'message': 'You need to activate your account first. '
                               'An email was sent to your inbox with the activation link'
                }, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({
                'status': 'Unauthorized',
                'message': 'Username/password combination invalid.'
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
