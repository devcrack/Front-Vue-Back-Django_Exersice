from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient


user_model = get_user_model()


def create_user() -> user_model:
    return user_model.objects.create_user(**{'username': 'a_user',
                                             'email': 'a_user@mail.com',
                                             'password': 'mientras123',
                                             'first_name': 'Soap',
                                             'last_name': 'Mctavish'
                                             })


def create_user_and_add_to_group(group_name) -> user_model:
    user = create_user()
    group = Group.objects.filter(name=group_name).first()
    user.groups.add(group)

    return user


def create_super_user():
    return user_model.objects.create_superuser(**{'username': 'admin',
                                                  'email': 'admin@mail.com',
                                                  'password': 'mientras123',
                                                  'first_name': 'Toro',
                                                  'last_name': 'Max'
                                                  })


def create_token(_user) -> Token:
    return Token.objects.create(user=_user)


def get_authenticated_client(token) -> APIClient:
    client = APIClient()

    client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    return client
