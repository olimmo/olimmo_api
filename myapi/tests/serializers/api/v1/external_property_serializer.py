import pytest
from rest_framework.exceptions import ValidationError
from myapi.serializers.api.v1.external_property_serializer import (
    ExternalPropertySerializer,
)
from myapi.tests.factories import ExternalPropertyFactory


class TestExternalPropertySerializer:
    def test_valid_serializer(self):
        external_property = ExternalPropertyFactory()

        # Run
        serializer = ExternalPropertySerializer(instance=external_property)

        # Check
        expected_data = {
            "id": external_property.id,
            "title": external_property.title,
            "surface": external_property.surface,
            "city": external_property.city,
            "created_at": external_property.created_at.strftime(
                "%Y-%m-%dT%H:%M:%S.%fZ"
            ),
            "currency": external_property.currency,
            "description": external_property.description,
            "elevator": external_property.elevator,
            "energy_rate": external_property.energy_rate,
            "first_photo_url": external_property.first_photo_url,
            "floor_number": external_property.floor_number,
            "gps_latitude": str(external_property.gps_latitude),
            "gps_longitude": str(external_property.gps_longitude),
            "greenhouse_gas": external_property.greenhouse_gas,
            "nb_bedrooms": external_property.nb_bedrooms,
            "nb_floors_building": external_property.nb_floors_building,
            "nb_parkings": external_property.nb_parkings,
            "nb_rooms": external_property.nb_rooms,
            "outside_access": external_property.outside_access,
            "postal_code": external_property.postal_code,
            "price": external_property.price,
            "property_type": external_property.property_type,
            "region": external_property.region,
            "seller_email": external_property.seller_email,
            "seller_name": external_property.seller_name,
            "seller_phone": external_property.seller_phone,
            "source": external_property.source,
            "source_id": external_property.source_id,
            "updated_at": external_property.updated_at.strftime(
                "%Y-%m-%dT%H:%M:%S.%fZ"
            ),
            "url": external_property.url,
        }

        serialized_data = dict(expected_data)

        assert serializer.data == serialized_data

    def test_invalid_serializer(self):
        invalid_data = {"external_property": ExternalPropertyFactory().id}

        serializer = ExternalPropertySerializer(data=invalid_data)

        with pytest.raises(ValidationError):
            serializer.is_valid(raise_exception=True)
