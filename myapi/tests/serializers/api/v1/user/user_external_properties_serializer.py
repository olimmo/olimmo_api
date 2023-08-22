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
        serializer = UserExternalPropertyRetrieveSerializer(
            instance=user_external_property
        )

        # Check
        expected_data = {
            "id": user_external_property.id,
            "created_at": user_external_property.created_at.strftime(
                "%Y-%m-%dT%H:%M:%S.%fZ"
            ),
            "state": user_external_property.state,
            "updated_at": user_external_property.updated_at.strftime(
                "%Y-%m-%dT%H:%M:%S.%fZ"
            ),
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

        expected_data = {"state": self.property_instance.state}
        serialized_data = dict(expected_data)

        assert serializer.data == serialized_data

    def test_invalid_serializer(self):
        data = {"state": ""}
        serializer = UserExternalPropertyUpdateSerializer(
            instance=self.property_instance, data=data
        )

        assert not serializer.is_valid()
        assert "state" in serializer.errors
