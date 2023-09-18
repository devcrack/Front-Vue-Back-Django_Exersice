# stdl-lib
import json

# 3rd-party
import pytest
from rest_framework import status

import Products.models

# Local
from Products.models import Category

from utils.boilerplate import (
    create_token,
    get_authenticated_client,
    create_user_and_add_to_group)

pytestmark = pytest.mark.django_db

url_products_list_create = '/an_api/categories/'

payload_category = {
    'name': 'Juguetes'
}


def create_normal_user_and_get_token(grou_name):
    user = create_user_and_add_to_group(grou_name)
    token = create_token(user)

    return token


def do_request_create_category(group_name):
    client = get_authenticated_client(create_normal_user_and_get_token(group_name))
    response = client.post(path=url_products_list_create, data=payload_category)
    return response.status_code


def test_create_category_by_manager_should_pass() -> None:
    assert do_request_create_category('manager') == status.HTTP_201_CREATED


def test_create_category_by_worker_should_pass() -> None:
    assert do_request_create_category('worker') == status.HTTP_201_CREATED


def test_create_category_by_consumer_should_fail() -> None:
    assert do_request_create_category('consumer') == status.HTTP_403_FORBIDDEN


def test_list_categories_should_pass():
    category = Category.objects.create(name='Juguetes')
    client = get_authenticated_client(create_normal_user_and_get_token('worker'))

    response = client.get(url_products_list_create)

    assert response.status_code == status.HTTP_200_OK
    content_response = [{'id': str(category.id), 'name': 'Juguetes', 'description': None}]

    assert response.json() == content_response
