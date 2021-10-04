import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient

from animals.enums import Gender
from animals.models import AnimalType, AnimalProperty, Animal

__alL__ = [
    'create_jwt_token',
    'create_animals',
]


@pytest.mark.django_db
@pytest.fixture
def create_jwt_token(request):
    request.cls.client = APIClient()
    request.cls.test_user = User.objects.create_user(
        username='test',
        email='test@mail.com',
        password='111'
    )

    resp = request.cls.client.post(
        '/api/token', {'username': 'test', 'password': '111'}, format='json'
    )
    request.cls.token = resp.data['access']
    request.cls.refresh = resp.data['refresh']
    request.cls.client.credentials(HTTP_AUTHORIZATION="Bearer " + request.cls.token)


@pytest.mark.django_db
@pytest.fixture
def create_animals(request):
    request.cls.animal_type = AnimalType.objects.create(name='Подводные')
    request.cls.animal_property = AnimalProperty.objects.create(name='Млекопитающие')
    request.cls.user = User.objects.create_user(
        username='test',
        email='test@mail.com',
        password='111'
    )
    request.cls.animal = Animal.objects.create(
        name='Тюлень',
        lat_title='Phocidae',
        gender=Gender.WOMAN,
        age=12,
        description='TEST',
        owner=request.cls.user,
    )
