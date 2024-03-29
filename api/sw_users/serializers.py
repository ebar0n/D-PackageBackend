from rest_framework import serializers
from sw_users.models import ClientAccount, ServiceAccount, UserAccount
from sw_vehicles.models import Vehicle
from sw_vehicles.serializers import VehicleSerializer


class UserAccountSerializer(serializers.ModelSerializer):
    """
        UserAccount Serializer
    """

    class Meta:
        model = UserAccount
        fields = (
            'id', 'first_name', 'last_name', 'email', 'password'
        )
        read_only_fields = ('id',)
        extra_kwargs = {'password': {'write_only': True}}


class ClientAccountSerializer(serializers.ModelSerializer):
    """
        ClientAccount Serializer
    """
    useraccount = UserAccountSerializer()

    class Meta:
        model = ClientAccount
        fields = ('id', 'useraccount', 'phone')
        read_only_fields = ('id',)

    def create(self, validated_data):
        data_user = validated_data.pop('useraccount')

        client = ClientAccount.objects.create(**validated_data)

        password = data_user.pop('password')
        user = UserAccount.objects.create(client=client, **data_user)
        user.set_password(password)
        user.save()

        return client


class ServiceAccountSerializer(serializers.ModelSerializer):
    """
        ServiceAccount Serializer
    """
    useraccount = UserAccountSerializer()
    vehicle = VehicleSerializer()

    class Meta:
        model = ServiceAccount
        fields = (
            'id', 'useraccount', 'phone', 'photo', 'birthdate',
            'address', 'identity_card', 'driver_license', 'vehicle'
        )
        read_only_fields = ('id',)

    def create(self, validated_data):
        data_user = validated_data.pop('useraccount')
        data_vehicle = validated_data.pop('vehicle')

        vehicle = Vehicle.objects.create(**data_vehicle)
        service = ServiceAccount.objects.create(vehicle=vehicle, **validated_data)

        password = data_user.pop('password')
        user = UserAccount.objects.create(service=service, **data_user)
        user.set_password(password)
        user.save()

        return service


class LoginSerializer(serializers.Serializer):
    """
    Login Serializer
    """
    username = serializers.CharField(max_length=128)
    password = serializers.CharField(max_length=128)


class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()


class ResetPasswordChangeSerializer(serializers.Serializer):
    email = serializers.EmailField()
    token = serializers.CharField(max_length=40)
    password = serializers.CharField(min_length=8, max_length=128)


class ChangePasswordSerializer(serializers.Serializer):
    """
    ChangePassword Serializer

    """
    old_password = serializers.CharField(max_length=128)
    new_password = serializers.CharField(min_length=8, max_length=128)


class CardCreateSerializer(serializers.Serializer):
    """
        Create card Serializer
    """
    stripe_token = serializers.CharField(max_length=100)


class CardDefaultSerializer(serializers.Serializer):
    """
        Default card Serializer
    """
    id = serializers.CharField(max_length=50, required=False)


class CardSerializer(serializers.Serializer):
    """
        Card Serializer
    """
    id = serializers.CharField(max_length=50)
    cvc_check = serializers.CharField(max_length=15)
    brand = serializers.CharField(max_length=50)
    exp_month = serializers.IntegerField()
    exp_year = serializers.IntegerField()
    funding = serializers.CharField(max_length=15)
    last4 = serializers.CharField(max_length=4)
    name = serializers.CharField(max_length=50)
