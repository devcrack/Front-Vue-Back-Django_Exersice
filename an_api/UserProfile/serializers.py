# 3rd-party
from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth import get_user_model


class CustomUserSerializer(RegisterSerializer):
    first_name = serializers.CharField(max_length=150, allow_blank=True, required=False)
    last_name = serializers.CharField(max_length=150, allow_blank=False, required=True)
    email = serializers.EmailField(allow_blank=False)

    def validate_email(self, email):
        user_model = get_user_model()
        if user_model.objects.filter(email=email).first():
            raise serializers.ValidationError("Email already exist. Type an unique email")
        return email
