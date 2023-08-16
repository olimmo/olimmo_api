from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response

from myapi.models import UserExternalProperty
from myapi.serializers.api.v1.user.user_external_property_serializer import (
    UserExternalPropertyRetrieveSerializer,
    UserExternalPropertyUpdateSerializer,
)
from .mixins import UserAuthenticationMixin


class UserExternalPropertyList(UserAuthenticationMixin, APIView):
    def get(self, request, *args, **kwargs):
        properties = UserExternalProperty.objects.filter(user=self.current_user)
        serializer = UserExternalPropertyRetrieveSerializer(properties, many=True)
        return Response(serializer.data)


class SingleUserExternalProperty(UserAuthenticationMixin, APIView):
    def get(self, request, user_external_property_id, *args, **kwargs):
        property = self._get_user_external_property(user_external_property_id)
        serializer = UserExternalPropertyRetrieveSerializer(property)
        return Response(serializer.data)

    def put(self, request, user_external_property_id, *args, **kwargs):
        property = self._get_user_external_property(user_external_property_id)
        serializer = UserExternalPropertyUpdateSerializer(
            instance=property, data=request.data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def _get_user_external_property(self, user_external_property_id):
        return get_object_or_404(
            UserExternalProperty, user=self.current_user, pk=user_external_property_id
        )
