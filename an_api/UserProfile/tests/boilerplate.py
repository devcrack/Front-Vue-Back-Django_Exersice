from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

user_model = get_user_model()


def create_user(**kwargs) -> user_model:
    return user_model.objects.create_user(**kwargs)


def create_token(_user):
    return Token.objects.create(user=_user)

