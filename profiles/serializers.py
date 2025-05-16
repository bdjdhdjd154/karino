from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profiles

class RegisterSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(write_only=True)
    last_name = serializers.CharField(write_only=True)
    phone_number=serializers.IntegerField(write_only=True)
    email = serializers.EmailField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email','first_name', 'last_name' , 'phone_number']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        first_name = validated_data.pop('first_name')
        last_name = validated_data.pop('last_name')
        phone_number=validated_data.pop('phone_number' , None)
        email = validated_data.pop('email')

        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            first_name=first_name,
            last_name=last_name,
            email=email
        )

        Profiles.objects.create(
            user=user,
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number
        )

        return user

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profiles
        fields='__all__'