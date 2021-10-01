import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient


@pytest.mark.django_db
@pytest.fixture(scope='class')
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
    request.cls.token = resp.data['token']
    request.cls.refresh = resp.data['refresh']
    request.cls.client.credentials(HTTP_AUTHORIZATION="Bearer " + request.cls.token)
