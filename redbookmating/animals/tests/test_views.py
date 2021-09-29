import pytest
from rest_framework import status


@pytest.mark.userfixtures('create_jwt_token')
@pytest.mark.django_db
class TestAnimalView:
    """Test animal api."""
    def test_get_animals_list(self):
        res = self.client.get('/animals/')
        assert res.status_code == status.HTTP_200_OK
