import pytest
from rest_framework.request import Request
from rest_framework.test import APIRequestFactory

from accounts.serializers import UserSerializer


@pytest.mark.usefixtures('create_animals')
@pytest.mark.django_db
class TestUserSerializer:
    def test_valid_data(self):
        data = {'username': 'test_user', 'password': '111'}
        serializer_data = UserSerializer(data=data)
        assert serializer_data.is_valid()

    def test_empty_data(self):
        data = {}
        serializer_data = UserSerializer(data=data)
        assert not serializer_data.is_valid()

    def test_read_data(self):
        factory = APIRequestFactory()
        request = factory.get('/')

        serializer_context = {
            'request': Request(request),
        }
        serialized_data = UserSerializer(instance=self.user, context=serializer_context)
        assert serialized_data['username'].value == self.user.username
