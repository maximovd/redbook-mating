from drf_yasg.utils import swagger_auto_schema
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response

from .models import Animal, AnimalType, AnimalProperty
from .serializers import (
    AnimalCreateUpdateDestroySerializer,
    AnimalListRetrieveSerializer,
    AnimalImageLoadSerializer,
    AnimalTypeSerializer,
    AnimalPropertySerializer,
)


class AnimalTypeViewSet(generics.ListAPIView):
    queryset = AnimalType.objects.all()
    serializer_class = AnimalTypeSerializer

class AnimalPropertyViewSet(generics.ListAPIView):
    queryset = AnimalProperty.objects.all()
    serializer_class = AnimalPropertySerializer


class AnimalListCreateView(generics.ListAPIView, generics.CreateAPIView):
    queryset = Animal.objects.get_queryset()
    serializer_class = AnimalCreateUpdateDestroySerializer

    @swagger_auto_schema(
        request=AnimalListRetrieveSerializer,
        responses={200: AnimalListRetrieveSerializer(many=True)}
    )
    def get(self, request):
        queryset = self.get_queryset()
        serializer = AnimalListRetrieveSerializer(queryset, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        request=AnimalCreateUpdateDestroySerializer,
        responses={200: AnimalListRetrieveSerializer()}
    )
    def post(self, request):
        serializer_in = AnimalCreateUpdateDestroySerializer(data=request.data)
        serializer_in.is_valid(raise_exception=True)
        animal = serializer_in.save()
        serializer_out = AnimalListRetrieveSerializer(instance=animal)
        return Response(serializer_out.data, status=status.HTTP_201_CREATED)


class AnimalRetrieveUpdateDestroyView(
    generics.RetrieveAPIView,
    generics.UpdateAPIView,
    generics.DestroyAPIView
):
    queryset = Animal.objects.get_queryset()
    serializer_class = AnimalCreateUpdateDestroySerializer
    # TODO Add permission classes

    @swagger_auto_schema(
        request=AnimalListRetrieveSerializer,
        responses={200: AnimalListRetrieveSerializer()}
    )
    def get(self, request, pk, *args, **kwargs):
        animal = generics.get_object_or_404(self.get_queryset(), pk=pk)
        serializer = AnimalListRetrieveSerializer(animal)
        return Response(serializer.data)

    @swagger_auto_schema(
        request=AnimalCreateUpdateDestroySerializer,
        responses={200: AnimalListRetrieveSerializer()},
    )
    def patch(self, request, pk):
        old_animal = generics.get_object_or_404(self.get_queryset(), pk=pk)
        serializer_in = AnimalCreateUpdateDestroySerializer(
            instance=old_animal,
            data=request.data,
            partial=True,
        )
        new_animal = serializer_in.save()
        serializer_out = AnimalListRetrieveSerializer(new_animal)
        return Response(serializer_out.data)

    @swagger_auto_schema(
        request=AnimalListRetrieveSerializer,
        responses={200: AnimalListRetrieveSerializer()},
    )
    def put(self, request, pk):
        old_animal = generics.get_object_or_404(self.get_queryset(), )
        pass
        # TODO Finish it

