from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .helpers.response import handle_serialized_data
from myapi.models import Property
from myapi.serializers import PropertySerializer


class PropertyList(APIView):
    def get(self, request, format=None):
        properties = Property.objects.all()
        serializer = PropertySerializer(properties, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PropertySerializer(data=request.data)
        return handle_serialized_data(serializer)


class PropertyDetail(APIView):
    def get_object(self, pk):
        return get_object_or_404(Property, pk=pk)

    def get(self, request, pk, format=None):
        property = self.get_object(pk)
        serializer = PropertySerializer(property)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        property = self.get_object(pk)
        serializer = PropertySerializer(property, data=request.data)
        return handle_serialized_data(serializer)

    def delete(self, request, pk, format=None):
        property = self.get_object(pk)
        property.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
