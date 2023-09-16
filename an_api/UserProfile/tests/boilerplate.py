from django.contrib.auth import get_user_model
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


def create_super_user():
    return user_model.objects.create_superuser(**{'username': 'admin',
                                                  'email': 'admin@mail.com',
                                                  'password': 'mientras123',
                                                  'first_name': 'Toro',
                                                  'last_name': 'Max'
                                                  })


def create_token(_user):
    return Token.objects.create(user=_user)


def get_authenticated_client(token):
    client = APIClient()

    client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    return client
