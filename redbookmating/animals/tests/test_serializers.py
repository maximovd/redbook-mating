import pytest

from animals.serializers import AnimalTypeSerializer, AnimalPropertySerializer, AnimalSerializer


@pytest.mark.usefixtures('create_animals')
@pytest.mark.django_db
class TestAnimalTypeSerializer:
    def test_valid_data(self):
        data = {'name': 'test_name'}
        serializer_data = AnimalTypeSerializer(data=data)
        assert serializer_data.is_valid()

    def test_empty_data(self):
        data = {}
        serializer_data = AnimalTypeSerializer(data=data)
        assert not serializer_data.is_valid()

    def test_read_data(self):
        serialized_data = AnimalTypeSerializer(instance=self.animal_type)
        assert serialized_data['name'].value == self.animal_type.name


@pytest.mark.usefixtures('create_animals')
@pytest.mark.django_db
class TestAnimalProperties:
    def test_valid_data(self):
        data = {'name': 'test_properties'}
        serializer_data = AnimalPropertySerializer(data=data)
        assert serializer_data.is_valid()

    def test_empty_data(self):
        data = {}
        serializer_data = AnimalPropertySerializer(data=data)
        assert not serializer_data.is_valid()

    def test_read_data(self):
        serialized_data = AnimalPropertySerializer(instance=self.animal_property)
        assert serialized_data['name'].value == self.animal_property.name


@pytest.mark.usefixtures('create_animals')
@pytest.mark.django_db
class TestAnimal:
    def test_valid_data(self):
        data = {
            "name": "animal",
            "lat_title": "animal",
            "gender": "M",
            "age": 6,
            "type": self.animal_type.id,
            "properties": [
                self.animal_property.id
            ],
            "description": "test animal",
            "owner": self.user.id,
            "location": "POINT(+27.182968 +23.119798)"
        }
        serializer_data = AnimalSerializer(data=data)
        flag = serializer_data.is_valid()
        assert flag is True

    def test_read_data(self):
        serialized_data = AnimalSerializer(instance=self.animal)
        assert serialized_data['name'].value == self.animal.name

    def test_invalid_data(self):
        data = {
            "name": "test animal",
            "lat_title": "animal",
            "gender": "M",
            "age": 6,
            "type": 1,
            "properties": [
                1
            ],
            "description": "test animal",
            "owner": 1,
            "location": "invalid"
        }
        serializer_data = AnimalSerializer(data=data)
        assert not serializer_data.is_valid()

    def test_empty_data(self):
        data = {}
        serializer_data = AnimalSerializer(data=data)
        assert not serializer_data.is_valid()
