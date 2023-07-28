from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from myapi.serializers.api.v1.lobstr.leboncoin.external_property_serializer import (
    ExternalPropertySerializer,
)


class ExternalPropertyListView(APIView):
    def post(self, request, format=None):
        serializer = ExternalPropertySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
