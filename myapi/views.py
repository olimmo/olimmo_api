from rest_framework import viewsets

from .serializers import PropertySerializer
from .models import Property


class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all().order_by("title")
    serializer_class = PropertySerializer
