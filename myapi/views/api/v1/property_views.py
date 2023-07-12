from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from myapi.models import Property
from myapi.serializers.api.v1 import PropertySerializer
from myapi.views.api.v1.helpers.response import render_serialized_data


class PropertyListView(APIView):
    def get(self, request, format=None):
        properties = Property.objects.all()
        serializer = PropertySerializer(properties, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PropertySerializer(data=request.data)
        return render_serialized_data(serializer)


class PropertyDetailView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Property, pk=pk)

    def get(self, request, pk, format=None):
        property = self.get_object(pk)
        serializer = PropertySerializer(property)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        property = self.get_object(pk)
        serializer = PropertySerializer(property, data=request.data)
        return render_serialized_data(serializer)

    def delete(self, request, pk, format=None):
        property = self.get_object(pk)
        property.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
