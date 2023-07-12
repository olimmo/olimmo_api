from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from myapi.models import Seller
from myapi.serializers.api.v1.seller import PropertySerializer
from myapi.views.api.v1.helpers.response import render_serialized_data


class PropertyListView(APIView):
    def get(self, request, seller_id, format=None):
        seller = self.__get_seller(seller_id)
        properties = seller.properties.all()
        serializer = PropertySerializer(properties, many=True)
        return Response(serializer.data)

    def post(self, request, seller_id, format=None):
        seller = self.__get_seller(seller_id)
        serializer = PropertySerializer(data=request.data)
        return render_serialized_data(serializer, save_kwargs={"seller": seller})

    # Private methods
    def __get_seller(self, seller_id):
        return get_object_or_404(Seller, pk=seller_id)


class PropertyDetailView(APIView):
    def get(self, request, seller_id, property_id, format=None):
        property = self.__get_property(seller_id, property_id)
        serializer = PropertySerializer(property)
        return Response(serializer.data)

    def put(self, request, seller_id, property_id, format=None):
        property = self.__get_property(seller_id, property_id)
        serializer = PropertySerializer(property, data=request.data)
        return render_serialized_data(serializer)

    def delete(self, request, seller_id, property_id, format=None):
        property = self.__get_property(seller_id, property_id)
        property.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # Private methods
    def __get_property(self, seller_id, property_id):
        seller = get_object_or_404(Seller, pk=seller_id)
        return get_object_or_404(seller.properties, pk=property_id)
