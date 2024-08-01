import pytest
from rest_framework.test import APIClient


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
@pytest.mark.db
def user(django_user_model):
    user = django_user_model.objects.create_user(
        username='testuser',
        email='testuser@example.com',
        password='123456Ab?'
    )
    return user


@pytest.fixture
@pytest.mark.db
def second_user(django_user_model):
    user = django_user_model.objects.create_user(
        username='testuser2',
        email='testuser2@example.com',
        password='123456Ab?'
    )
    return user
