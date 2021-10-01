from django.contrib.gis import measure
from rest_framework import status
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from redbookmating import settings
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

    @action(detail=True, methods=['get'])
    def get_nearby(self, request, pk=None) -> Response:
        """Get nearby animals over target animal."""
        km = request.data.get('km', settings.DEFAULT_SEARCH_DISTANCE)
        try:
            found_animal = Animal.objects.get(id=pk)
        except (Animal.DoesNotExist, Animal.MultipleObjectsReturned):
            return Response({'text': 'Animal does not exist'}, status=status.HTTP_404_NOT_FOUND)
        distance_from_point = {'km': km}
        nearby_animals = Animal.objects.filter(
            location__distance_lte=(found_animal.location, measure.D(**distance_from_point)),
            type=found_animal.type,
        ).exclude(id=pk)
        nearby_animals_serializable = AnimalSerializer(nearby_animals, many=True)
        return Response(nearby_animals_serializable.data, status=status.HTTP_200_OK)
