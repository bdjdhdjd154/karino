from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profiles

class RegisterSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(write_only=True)
    first_name = serializers.CharField(write_only=True)
    last_name = serializers.CharField(write_only=True)
    email = serializers.EmailField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'phone_number', 'first_name', 'last_name']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        phone = validated_data.pop('phone_number')
        first_name = validated_data.pop('first_name')
        last_name = validated_data.pop('last_name')
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
            phone_number=phone,
            first_name=first_name,
            last_name=last_name
        )

        return user

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profiles
        feilds= '__all__'    