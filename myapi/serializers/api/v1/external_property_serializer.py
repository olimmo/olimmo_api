from rest_framework import serializers

from myapi.models import ExternalProperty


class ExternalPropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = ExternalProperty
        fields = "__all__"
