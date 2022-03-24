from django.contrib.auth.models import User
from rest_framework import serializers


class UserDefaultSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = serializers.ALL_FIELDS
