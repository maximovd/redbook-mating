import pytest
from django.contrib.auth.models import User


@pytest.mark.django_db
class TestUserModel:
    def test_create(self):
        User.objects.create(username='test', password=111, email='admin@mail.com')

        assert User.objects.get(username='test').email == 'admin@mail.com'
