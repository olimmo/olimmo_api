import pytest
from rest_framework.exceptions import ValidationError
from myapi.serializers.api.v1.user.user_external_property_serializer import (
    UserExternalPropertyRetrieveSerializer,
    UserExternalPropertyUpdateSerializer,
)
from myapi.tests.factories import (
    UserExternalPropertyFactory,
    ExternalPropertyFactory,
)


class TestUserExternalPropertyRetrieveSerializer:
    def test_valid_serializer(self):
        user_external_property = UserExternalPropertyFactory()

        # Run
        serializer = UserExternalPropertyRetrieveSerializer(
            instance=user_external_property
        )

        # Extracting external_property for readability
        ep = user_external_property.external_property

        # Check
        expected_data = {
            "id": user_external_property.id,
            "external_property": {
                "id": ep.id,
                "title": ep.title,
                "surface": ep.surface,
                "city": ep.city,
                "currency": ep.currency,
                "description": ep.description,
                "elevator": ep.elevator,
                "energy_rate": ep.energy_rate,
                "first_photo_url": ep.first_photo_url,
                "floor_number": ep.floor_number,
                "gps_latitude": str(ep.gps_latitude),
                "gps_longitude": str(ep.gps_longitude),
                "greenhouse_gas": ep.greenhouse_gas,
                "nb_bedrooms": ep.nb_bedrooms,
                "nb_floors_building": ep.nb_floors_building,
                "nb_parkings": ep.nb_parkings,
                "nb_rooms": ep.nb_rooms,
                "outside_access": ep.outside_access,
                "postal_code": ep.postal_code,
                "price": ep.price,
                "property_type": ep.property_type,
                "region": ep.region,
                "seller_email": ep.seller_email,
                "seller_name": ep.seller_name,
                "seller_phone": ep.seller_phone,
                "source": ep.source,
                "source_id": ep.source_id,
                "url": ep.url,
            },
            "state": user_external_property.state,
            "user": user_external_property.user.id,
        }

        serialized_data = dict(expected_data)

        assert serializer.data == serialized_data

    def test_invalid_serializer(self):
        invalid_data = {"external_property": ExternalPropertyFactory().id}

        serializer = UserExternalPropertyRetrieveSerializer(data=invalid_data)

        with pytest.raises(ValidationError):
            serializer.is_valid(raise_exception=True)


class TestUserExternalPropertyUpdateSerializer:
    def setup_method(self):
        self.property_instance = UserExternalPropertyFactory()

    def test_valid_serializer(self):
        data = {"state": "waiting"}
        serializer = UserExternalPropertyUpdateSerializer(
            instance=self.property_instance, data=data
        )

        assert serializer.is_valid()
        serializer.save()

        expected_data = {
            "state": self.property_instance.state,
        }

        serialized_data = dict(expected_data)

        assert serializer.data == serialized_data

    def test_invalid_serializer(self):
        data = {"state": ""}
        serializer = UserExternalPropertyUpdateSerializer(
            instance=self.property_instance, data=data
        )

        assert not serializer.is_valid()
        assert "state" in serializer.errors
