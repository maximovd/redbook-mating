from django.db import transaction
from rest_framework import serializers

from helpers.serializers import ExcludedSerializer
from helpers.urls import get_animal_image
from .models import Animal, AnimalType, AnimalProperty


class AnimalTypeSerializer(ExcludedSerializer):
    class Meta:
        model = AnimalType
        fields = '__all__'


class AnimalPropertySerializer(ExcludedSerializer):
    class Meta:
        model = AnimalProperty
        fields = '__all__'


class AnimalListRetrieveSerializer(ExcludedSerializer):
    """Serializer work with animals list."""
    gender = serializers.CharField(source='get_gender_display')
    animal_type = AnimalTypeSerializer()
    animal_properties = AnimalPropertySerializer()
    image = serializers.SerializerMethodField()

    def get_image(self, obj):
        return get_animal_image(obj)

    class Meta:
        model = Animal


class AnimalCreateUpdateDestroySerializer(ExcludedSerializer):
    """Serializer create, update and destroy animals object."""
    class Meta:
        model = Animal

    @transaction.atomic
    def create(self, validated_data, *args, **kwargs):
        type_name = str(validated_data.pop('animal_type', ''))
        animal_type = AnimalType.objects.get(name=type_name)
        # TODO Validate animal type
        validated_data['type'] = animal_type
        return super().create(validated_data)

    @transaction.atomic
    def update(self, instance, validate_data, *args, **kwargs):
        type_name = str(validate_data.pop('animal_type', ''))
        if type_name:
            animal_type = AnimalType.objects.get(name=type_name)
            validate_data['type'] = animal_type
        return super().update(instance, validate_data)


class AnimalImageLoadSerializer(serializers.ModelSerializer):
    """Serializer load image into animal object."""
    class Meta:
        model = Animal
        fields = ('image',)
