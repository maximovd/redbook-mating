from django.conf import settings
from django.db import transaction
from rest_framework import serializers

from helpers.serializers import ExcludedSerializer
from .models import Animal, AnimalType, AnimalProperty


class AnimalCreateUpdateDestroySerializer(ExcludedSerializer):
    class Meta:
        model = Animal

    @transaction.atomic
    def create(self, validated_data, *args, **kwargs):
        pass  # TODO Create Serializer
