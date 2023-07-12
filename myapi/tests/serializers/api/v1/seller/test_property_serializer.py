import pytest
from myapi.serializers.api.v1.seller import PropertySerializer
from myapi.models import Property


@pytest.fixture
def property_data():
    return {
        "city": "New York",
        "surface": 1500,
        "title": "Spacious Apartment",
    }


def test_property_serializer_valid(property_data):
    serializer = PropertySerializer(data=property_data)
    assert serializer.is_valid()


def test_property_serializer_save():
    property_data = {
        "city": "New York",
        "surface": 1500,
        "title": "Spacious Apartment",
    }
    serializer = PropertySerializer(data=property_data)
    assert serializer.is_valid()
    property = serializer.save()  # Save the validated data
    assert Property.objects.count() == 1
    assert property.city == "New York"
    assert property.surface == 1500
    assert property.title == "Spacious Apartment"
