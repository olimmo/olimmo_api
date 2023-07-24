from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from myapi.models import Seller
from myapi.serializers.api.v1.seller import PropertySerializer
from .base_views import BaseView


class PropertyListView(APIView):
    def get(self, request, seller_id, format=None):
        seller = get_object_or_404(Seller, pk=seller_id)
        properties = seller.properties.all()
        serializer = PropertySerializer(properties, many=True)
        return Response(serializer.data)

    def post(self, request, seller_id, format=None):
        seller = get_object_or_404(Seller, pk=seller_id)
        serializer = PropertySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(seller=seller)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PropertyDetailView(BaseView):
    def get(self, request, seller_id, property_id, format=None):
        property = self.__current_property(seller_id, property_id)
        serializer = PropertySerializer(property)
        return Response(serializer.data)

    def put(self, request, seller_id, property_id, format=None):
        property = self.__current_property(seller_id, property_id)
        serializer = PropertySerializer(property, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(seller=self.current_seller(seller_id))
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, seller_id, property_id, format=None):
        property = self.__current_property(seller_id, property_id)
        property.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def __current_property(self, seller_id, property_id):
        return get_object_or_404(
            self.current_seller(seller_id).properties, pk=property_id
        )
