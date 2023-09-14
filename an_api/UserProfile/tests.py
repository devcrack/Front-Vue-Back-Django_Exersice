# stdl-lib
import json

# 3rd-party
import pytest
from rest_framework import status
from django.urls import reverse

registration_url = reverse('rest_register')

# @pytest.fixture
# def api_client():
#     return APIClient()

pytestmark = pytest.mark.django_db


def test_registration(client) -> None:
    registration_data = {
        'username': 'test@email.com',
        'password1': 'awesome_password',
        'password2': 'awesome_password',
        'email': 'test@email.com',
    }

    response = client.post(path=registration_url, data=registration_data)
    # response = client.post('/an_api/registration/', registration_data, format='json')

    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()

    assert 'key' in data


def test_registration_should_fail_password_to_short(client) -> None:
    registration_data = {
        'username': 'test@email.com',
        'password1': 'test',
        'password2': 'test',
        'email': 'test@email.com',
    }

    response = client.post(path=registration_url, data=registration_data)
    # response = client.post('/an_api/registration/', registration_data, format='json')

    assert response.status_code == status.HTTP_400_BAD_REQUEST

    body_error = {
        "password1": [
            "This password is too short. It must contain at least 8 characters.",
            "This password is too common."
        ]
    }

    print(json.loads(response.content))
    assert json.loads(response.content) == body_error
