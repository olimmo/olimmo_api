import pytest
from myapi.serializers.api.v1 import PropertySerializer
from myapi.models import Property
from myapi.tests.factories import PropertyFactory


@pytest.fixture
def property_data():
    return {
        "city": "New York",
        "postal_code": "12345",
        "surface": 1500,
        "title": "Spacious Apartment",
    }


def test_property_serializer_valid(property_data):
    serializer = PropertySerializer(data=property_data)
    assert serializer.is_valid()


def test_property_serializer_invalid_surface():
    property_data = {
        "city": "New York",
        "postal_code": "12345",
        "surface": -500,  # Invalid surface
        "title": "Spacious Apartment",
    }

    serializer = PropertySerializer(data=property_data)
    assert not serializer.is_valid()
    assert "surface" in serializer.errors
    assert (
        "Ensure this value is greater than or equal to 0."
        in serializer.errors["surface"]
    )


def test_property_serializer_invalid_postal_code():
    property_data = {
        "city": "New York",
        "postal_code": "1234567890abcdefghij",  # Invalid postal code length
        "surface": 1500,
        "title": "Spacious Apartment",
    }
    serializer = PropertySerializer(data=property_data)
    assert not serializer.is_valid()
    assert "postal_code" in serializer.errors
    assert (
        "Ensure this field has no more than 10 characters."
        in serializer.errors["postal_code"]
    )


def test_property_serializer_custom_fields():
    property = PropertyFactory(surface=2000)  # Create a Property using Factory Boy
    serializer = PropertySerializer(property)
    assert serializer.data["is_big"]


def test_property_serializer_save():
    property_data = {
        "city": "New York",
        "postal_code": "12345",
        "surface": 1500,
        "title": "Spacious Apartment",
    }
    serializer = PropertySerializer(data=property_data)
    assert serializer.is_valid()
    property = serializer.save()  # Save the validated data
    assert Property.objects.count() == 1
    assert property.city == "New York"
    assert property.postal_code == "12345"
    assert property.surface == 1500
    assert property.title == "Spacious Apartment"
