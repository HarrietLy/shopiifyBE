from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Address

class UserSerializer(serializers.ModelSerializer):
    # addresses = serializers.StringRelatedField(many=True)
    class Meta:
        model = User
        fields = ('id','username','password', 'is_superuser','date_joined','email','addresses')

class TokenSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=255)
    username = serializers.CharField(max_length=255)


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model= Address
        fields = ('id','shipping_address','user')