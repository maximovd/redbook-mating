import pytest

from animals.enums import Gender
from animals.models import Animal


@pytest.mark.django_db(transaction=True)
@pytest.mark.usefixtures('create_animals')
class TestAnimalModel:
    def test_create(self):
        Animal.objects.create(
            name='test',
            lat_title='lat test',
            gender=Gender.WOMAN,
            age=12,
            type=self.animal_type,
            properties=[self.animal_property],
            description='TEST TEST',
            owner=self.user
        )

    assert Animal.objects.get(name='test').lat_title == 'lat_test'
