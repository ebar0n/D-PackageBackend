from rest_framework import serializers

from .models import ClientAccount, UserAccount, ServiceAccount
from sw_vehicles.models import Vehicle

from sw_vehicles.serializers import VehicleSerializer


class UserAccountSerializer(serializers.ModelSerializer):
    """
        UserAccount Serializer
    """
    confirm_password = serializers.CharField(allow_blank=False, write_only=True)

    class Meta:
        model = UserAccount
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
            'confirm_password',)
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        if data['password'] != data.pop('confirm_password'):
            raise serializers.ValidationError(
                {'password': 'Passwords do not match!'})
        return data


class ClientAccountSerializer(serializers.ModelSerializer):
    """
        ClientAccount Serializer
    """
    useraccount = UserAccountSerializer()

    class Meta:
        model = ClientAccount
        fields = ('useraccount', 'phone')

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
            'useraccount',
            'phone',
            'photo',
            'birthdate',
            'address',
            'identity_card',
            'driver_license',
            'vehicle'
            )

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
