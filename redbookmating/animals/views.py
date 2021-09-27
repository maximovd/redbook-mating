from rest_framework import viewsets, permissions

from animals.models import AnimalType, AnimalProperty, Animal
from animals.serializers import AnimalTypeSerializer, AnimalPropertySerializer, AnimalSerializer


class AnimalTypeViewSet(viewsets.ModelViewSet):
    queryset = AnimalType.objects.all()
    serializer_class = AnimalTypeSerializer
    permission_classes = [permissions.IsAuthenticated]


class AnimalPropertyViewSet(viewsets.ModelViewSet):
    queryset = AnimalProperty.objects.all()
    serializer_class = AnimalPropertySerializer
    permission_classes = [permissions.IsAuthenticated]


class AnimalViewSet(viewsets.ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    permission_classes = [permissions.IsAuthenticated]
