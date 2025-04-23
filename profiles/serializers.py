from rest_framework import serializers
# Create your models here.
class Profiles(serializers.Serializer):
    phone_number =serializers.CharField(max_length=11)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=70)
    def create(self,validated_data):
        return Profiles.objects.create(**validated_data)
