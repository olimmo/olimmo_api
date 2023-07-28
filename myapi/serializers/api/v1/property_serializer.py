# serializers.py
from rest_framework import serializers

from myapi.models import Property


class PropertySerializer(serializers.ModelSerializer):
    full_address = serializers.SerializerMethodField()

    class Meta:
        model = Property
        fields = "__all__"

    # CUSTOM SERIALIZER FIELDS
    def get_full_address(self, obj):
        return " ".join([obj.address, obj.city, obj.postal_code, obj.country])

    # SERIALIZE VALIDATIONS
    def validate_surface(self, value):
        # additional validation only for the serializer
        if value <= 0:
            raise serializers.ValidationError("Surface must be greater than 0.")
        return value

    def validate(self, data):
        # additional validation only for the serializer
        if len(data["postal_code"]) > 10:
            raise serializers.ValidationError(
                "This postal code have to be longer than 10 characters"
            )
        return data
