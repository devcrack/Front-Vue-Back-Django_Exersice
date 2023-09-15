# stdl-lib
import json

# 3rd-party
import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token

from boilerplate import create_user, create_token


registration_url = reverse('custom_rest_register')


pytestmark = pytest.mark.django_db


def test_registration(client) -> None:
    registration_data = {
        'username': 'test@email.com',
        'password1': 'awesome_password',
        'password2': 'awesome_password',
        'email': 'test@email.com',
        "first_name": "Carlos",
        "last_name": "Pensantes"
    }

    response = client.post(path=registration_url, data=registration_data)

    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()

    assert 'key' in data


def test_registration_should_fail_password_to_short(client) -> None:
    registration_data = {
        'username': 'test@email.com',
        'password1': 'test',
        'password2': 'test',
        'email': 'test@email.com',
        "first_name": "Carlos",
        "last_name": "Pensantes"
    }

    response = client.post(path=registration_url, data=registration_data)

    assert response.status_code == status.HTTP_400_BAD_REQUEST

    body_error = {
        "password1": [
            "This password is too short. It must contain at least 8 characters.",
            "This password is too common."
        ]
    }

    assert json.loads(response.content) == body_error


def test_registration_should_fail_email_duplication(client) -> None:
    create_user(**{'username': 'a_username2',
                   'email': 'awesome_mail1@mail.com',
                   'password': 'mientras123',
                   'first_name': 'Carlos',
                   'last_name': 'Pensantes'
                   })

    registration_data = {'username': 'a_username2',
                         'email': 'awesome_mail1@mail.com',
                         'password1': 'mientras123',
                         'password2': 'mientras123',
                         'first_name': 'test_name',
                         'last_name': 'test_last_name'
                         }

    response = client.post(path=registration_url, data=registration_data)

    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_registration_should_fail_username_duplication(client) -> None:
    create_user(**{'username': 'a_username3',
                   'email': 'a_new_awesome_mail@mail.com',
                   'password': 'mientras123',
                   'first_name': 'test_name',
                   'last_name': 'test_last_name'
                   })

    registration_data = {'username': 'a_username3',
                         'email': 'awesome_mail@mail.com',
                         'password1': 'mientras123',
                         'password2': 'mientras123',
                         'first_name': 'test_name',
                         'last_name': 'test_last_name'
                         }

    response = client.post(path=registration_url, data=registration_data)

    body_error = {
        "username": [
            "A user with that username already exists."
        ]
    }

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert json.loads(response.content) == body_error


def test_login_success(client) -> None:

    create_user(**{'username': 'test_username',
                   'email': 'test@example.com',
                   'password': 'testpassword',
                   'first_name': 'test_name',
                   'last_name': 'test_last_name'
                   })

    response = client.post(path=reverse('rest_login'),
                           data={'email': 'test@example.com',
                                 'password': 'testpassword'})

    assert response.status_code == status.HTTP_200_OK


def test_logout_success() -> None:
    user = create_user(**{'username': 'test_username',
                          'email': 'test@example.com',
                          'password': 'testpassword',
                          'first_name': 'test_name',
                          'last_name': 'test_last_name'
                          })
    token = create_token(user)
    client = APIClient()

    client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    response = client.post(reverse('rest_logout'))

    assert response.status_code == status.HTTP_200_OK

    # Assert that a code block/function call raises an exception.
    with pytest.raises(Token.DoesNotExist):
        Token.objects.get(user=user)


def test_get_user_detail_should_pass() -> None:
    client = APIClient()


    registration_data = {
        'username': 'test@email.com',
        'password1': 'awesome_password',
        'password2': 'awesome_password',
        'email': 'test@email.com',
        "first_name": "Carlos",
        "last_name": "Pensantes"
    }

    response = client.post(path=registration_url, data=registration_data)
    print(json.loads(response.content))
    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()
    client.credentials(HTTP_AUTHORIZATION='Token ' + data.get('key'))
    response = client.get(reverse('rest_user_details'))

    assert response.status_code == status.HTTP_200_OK





