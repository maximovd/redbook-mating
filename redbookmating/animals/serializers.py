from rest_framework import serializers

from animals.models import Animal, AnimalType, AnimalProperty


class AnimalTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalType
        fields = ('name',)


class AnimalPropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalProperty
        fields = ('name',)


class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = [
            'name',
            'lat_title',
            'image',
            'gender',
            'age',
            'type',
            'properties',
            'description',
            'owner',
            'location',
        ]
