from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from myapi.models import Property
from myapi.serializers.api.v1 import PropertySerializer


class LeboncoinPropertyListView(APIView):
    def post(self, request, format=None):
        serializer = PropertySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
