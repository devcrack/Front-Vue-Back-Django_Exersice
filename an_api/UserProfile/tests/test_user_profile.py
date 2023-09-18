# stdl-lib

# 3rd-party
import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token

from utils.boilerplate import (create_super_user,
                               create_token,
                               create_user,
                               get_authenticated_client)

pytestmark = pytest.mark.django_db


def test_register_manager_user_should_succed() -> None:
    admin_user = create_super_user()

    token = create_token(admin_user)

    client = get_authenticated_client(token)

    payload = {
        'username': 'andrew',
        'email': 'andrea_del_arco@mail.com',
        'password1': 'mientras123',
        'password2': 'mientras123',
        'first_name': 'Andreita',
        'last_name': 'Bonita',
        'group': 'manager'
    }

    response = client.post(path=reverse('low_level_rest_register'),
                           data=payload)

    assert response.status_code == status.HTTP_201_CREATED

# DEPRECATED
# def test_create_lowest_level_users_should_pass() -> None:
#     user = create_user()
#     user.groups.add(Group.objects.get(name='manager'))
#
#     token = create_token(user)
#
#     client = get_authenticated_client(token)
#
#     payload = {
#         "username": "anton",
#         "email": "anton_del_arco@mail.com",
#         "password1": "mientras123",
#         "password2": "mientras123",
#         "first_name": "Antonello",
#         "last_name": "Feo",
#         "group": "worker"
#     }
#     response = client.post(path=reverse('lowest_level_rest_register'), data=payload)
#
#     assert response.status_code == status.HTTP_201_CREATED




def test_login_success(client) -> None:

    create_user()

    response = client.post(path=reverse('rest_login'),
                           data={'email': 'a_user@mail.com',
                                 'password': 'mientras123'})

    assert response.status_code == status.HTTP_200_OK


def test_logout_success() -> None:
    user = create_user()
    token = create_token(user)

    client = get_authenticated_client(token)

    response = client.post(reverse('rest_logout'))

    assert response.status_code == status.HTTP_200_OK

    # Assert that a code block/function call raises an exception.
    with pytest.raises(Token.DoesNotExist):
        Token.objects.get(user=user)


def test_get_user_detail_should_pass() -> None:
    user = create_user()
    token = create_token(user)

    client = get_authenticated_client(token)

    response = client.get(reverse('rest_user_details'))

    assert response.status_code == status.HTTP_200_OK





