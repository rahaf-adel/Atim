from rest_framework import serializers
from django.contrib.auth.models import User


class userRegisterSerializer(serializers.ModelSerializer):
    """A simple serializers that register user to the system"""
    class Meta:
        model = User
        fields = ['username', 'email', 'password']