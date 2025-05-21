
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Company

class CompanyRegisterSerializer(serializers.ModelSerializer):
    company_name = serializers.CharField(write_only=True)
    address = serializers.CharField(write_only=True)
    website = serializers.URLField(write_only=True, required=False)
    phone_number = serializers.CharField(write_only=True)
    email = serializers.EmailField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'company_name', 'phone_number','address','website']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        company_name = validated_data.pop('company_name'),
        address=validated_data.pop('address'),
        website=validated_data.pop('website'),
        phone_number = validated_data.pop('phone_number', None),
        email = validated_data.pop('email')

        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=email,
        )

        Company.objects.create(
            user=user,
            company_name=company_name,
            phone_number=phone_number,
            address=address,
            website=website

        )

        return user

class CompanyProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'