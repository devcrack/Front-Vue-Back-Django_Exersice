# 3rd-party
from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group


class CustomUserRegisterSerializer(RegisterSerializer):
    first_name = serializers.CharField(max_length=150, allow_blank=False, required=True)
    last_name = serializers.CharField(max_length=150, allow_blank=False, required=True)
    email = serializers.EmailField(allow_blank=False)

    def validate_email(self, email):
        user_model = get_user_model()
        if user_model.objects.filter(email=email).first():
            raise serializers.ValidationError("Email already exist. Type an unique email")
        return email


class LowLevelUserSerializer(CustomUserRegisterSerializer):
    group = serializers.CharField(max_length=8, allow_blank=False, required=True)

    @staticmethod
    def __group_exist(group):
        if not Group.objects.filter(name=group).exists():
            raise serializers.ValidationError("Provided Group Doesn't Exist")

    def validate_group(self, group):
        self.__group_exist(group)

        user = self.context['request'].user

        if not user.is_staff:
            if not group in ['consumer', 'worker']:
                raise serializers.ValidationError("The Provided Group is Not Valid")
        return group


class CustomUserSerializer(serializers.ModelSerializer):
    role = serializers.SerializerMethodField()

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email', 'role']

    @staticmethod
    def get_role(obj):
        group = obj.groups.all().first()
        return group.name