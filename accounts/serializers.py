from rest_framework import serializers
from django.contrib.auth.models import User 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','password', 'is_superuser')

class TokenSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=255)
    username = serializers.CharField(max_length=255)
