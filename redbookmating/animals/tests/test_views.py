import pytest
from rest_framework import status

from animals.models import AnimalType, AnimalProperty


@pytest.mark.usefixtures('create_jwt_token')
@pytest.mark.django_db
class TestAnimalView:
    """Test animal api."""

    def test_get_animals_list(self):
        res = self.client.get('/animals/')
        assert res.status_code == status.HTTP_200_OK

    def test_create_animals_type(self):
        res = self.client.post('/animals-type/', {'name': 'test'}, format='json')
        assert res.status_code == status.HTTP_201_CREATED

    def test_get_all_animals_types(self):
        res = self.client.get('/animals-type/')
        assert res.status_code == status.HTTP_200_OK

    def test_create_animals_properties(self):
        res = self.client.post('/animals-properties/', {'name': 'test'}, format='json')
        assert res.status_code == status.HTTP_201_CREATED

    def test_get_all_animals_properties(self):
        res = self.client.get('/animals-properties/')
        assert res.status_code == status.HTTP_200_OK

    def test_create_animals(self):
        # TODO Split and move to fixtures
        test_animal_type = AnimalType.objects.create(name='Подводные')
        test_animal_property = AnimalProperty.objects.create(name='Млекопитающие')
        data = {
            "name": "animal",
            "lat_title": "animal",
            "gender": "M",
            "age": 6,
            "type": test_animal_type.id,
            "properties": [
                test_animal_property.id
            ],
            "description": "test animal",
            "owner": self.test_user.id,
            "location": "POINT(+27.182968 +23.119798)"
        }
        res = self.client.post('/animals/', data, format='json')
        assert res.status_code == status.HTTP_201_CREATED

