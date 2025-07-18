from rest_framework import serializers
from .models import APIUsage

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

class APIUsageSerializer(serializers.ModelSerializer):
    class Meta:
        model = APIUsage
        fields = '__all__'

class ProfileSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
