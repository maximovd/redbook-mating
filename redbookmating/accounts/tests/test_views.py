import pytest
from rest_framework import status


@pytest.mark.usefixtures('create_jwt_token')
@pytest.mark.django_db
class TestUserView:
    """Test user api."""

    def test_get_users_list(self):
        res = self.client.get('/users/')
        assert res.status_code == status.HTTP_200_OK
