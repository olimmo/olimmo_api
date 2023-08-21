from rest_framework import viewsets, status
from rest_framework.response import Response
from myapi.filters.api.v1.user.user_external_property_filter import (
    UserExternalPropertyFilter,
)
from myapi.serializers.api.v1.user.user_external_property_serializer import (
    UserExternalPropertyRetrieveSerializer,
    UserExternalPropertyUpdateSerializer,
)
from .mixins import UserAuthenticationMixin

from myapi.models import UserExternalProperty


class UserExternalPropertyViewSet(UserAuthenticationMixin, viewsets.ModelViewSet):
    queryset = UserExternalProperty.objects.all()
    filterset_class = UserExternalPropertyFilter

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.current_user_external_properties)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def get_serializer_class(self):
        if self.action == "update":
            return UserExternalPropertyUpdateSerializer
        return UserExternalPropertyRetrieveSerializer
