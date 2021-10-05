import pytest

from animals.enums import Gender
from animals.models import Animal


@pytest.mark.usefixtures('create_animals')
@pytest.mark.django_db
class TestAnimalModel:
    def test_create(self):
        Animal.objects.create(
            name='test',
            lat_title='lat test',
            gender=Gender.WOMAN,
            age=12,
            type=self.animal_type,
            description='TEST TEST',
            owner=self.user
        )

        assert Animal.objects.get(name='test').lat_title == 'lat test'
