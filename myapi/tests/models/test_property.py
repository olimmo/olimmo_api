import pytest
from myapi.models import Property
from django.core.exceptions import ValidationError
from myapi.tests.factories import PropertyFactory


@pytest.fixture
def property():
    return PropertyFactory()


def test_property_creation(property):
    assert isinstance(property, Property)
    assert property.id is not None
    assert property.surface is not None
    assert property.title is not None


# Validations
def test_surface_validation():
    with pytest.raises(ValidationError):
        property = PropertyFactory(surface=-1000)  # Invalid value
        property.full_clean()

    with pytest.raises(ValidationError):
        property = PropertyFactory(surface=200000)  # Invalid value
        property.full_clean()


def test_title_validation():
    with pytest.raises(ValidationError):
        property = PropertyFactory(title="")  # Empty value
        property.full_clean()


# Properties
def test_full_address_with_all_components():
    property = PropertyFactory(
        address="123 Street", city="City", postal_code="12345", country="Country"
    )
    expected_address = "123 Street City 12345 Country"
    assert property.full_address == expected_address


def test_full_address_with_null_components():
    property = PropertyFactory(
        address="123 Street", city="City", postal_code=None, country=None
    )
    expected_address = "123 Street City"
    assert property.full_address == expected_address
