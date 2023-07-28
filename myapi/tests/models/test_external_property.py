import pytest
from myapi.models import ExternalProperty
from django.core.exceptions import ValidationError
from myapi.tests.factories import ExternalPropertyFactory


@pytest.fixture
def external_property():
    return ExternalPropertyFactory()


# Creation
def test_external_property_creation(external_property):
    assert isinstance(external_property, ExternalProperty)
    assert external_property.id is not None
    assert external_property.title is not None
    assert external_property.surface is not None
    assert external_property.city is not None
    assert external_property.currency is not None
    assert external_property.description is not None
    assert external_property.elevator is not None
    assert external_property.floor_number is not None
    assert external_property.postal_code is not None
    assert external_property.region is not None
    assert external_property.source is not None


# Validations
def test_title_validation():
    with pytest.raises(ValidationError):
        external_property = ExternalPropertyFactory(title="")  # Empty value
        external_property.full_clean()


def test_surface_validation():
    with pytest.raises(ValidationError):
        external_property = ExternalPropertyFactory(surface=-1)  # Invalid value
        external_property.full_clean()

    with pytest.raises(ValidationError):
        external_property = ExternalPropertyFactory(surface=100001)  # Invalid value
        external_property.full_clean()


def test_city_validation():
    with pytest.raises(ValidationError):
        external_property = ExternalPropertyFactory(city="")  # Empty value
        external_property.full_clean()


def test_currency_validation():
    with pytest.raises(ValidationError):
        external_property = ExternalPropertyFactory(currency="ABC")  # Invalid value
        external_property.full_clean()


def test_description_validation():
    with pytest.raises(ValidationError):
        external_property = ExternalPropertyFactory(description="")  # Empty value
        external_property.full_clean()


def test_first_photo_url_validation():
    with pytest.raises(ValidationError):
        external_property = ExternalPropertyFactory(
            first_photo_url="not a valid url"
        )  # Invalid URL
        external_property.full_clean()


def test_floor_number_validation():
    with pytest.raises(ValidationError):
        external_property = ExternalPropertyFactory(floor_number=-1)  # Invalid value
        external_property.full_clean()

    with pytest.raises(ValidationError):
        external_property = ExternalPropertyFactory(
            floor_number=100001
        )  # Invalid value
        external_property.full_clean()


def test_postal_code_validation():
    with pytest.raises(ValidationError):
        external_property = ExternalPropertyFactory(postal_code="")  # Empty value
        external_property.full_clean()


def test_region_validation():
    with pytest.raises(ValidationError):
        external_property = ExternalPropertyFactory(region="")  # Empty value
        external_property.full_clean()


def test_source_validation():
    with pytest.raises(ValidationError):
        external_property = ExternalPropertyFactory(source="")  # Empty value
        external_property.full_clean()


# Url validation
def test_url_validation():
    with pytest.raises(ValidationError):
        external_property = ExternalPropertyFactory(
            url="not a valid url"
        )  # Invalid URL
        external_property.full_clean()


# GPS Latitude and Longitude
def test_gps_latitude_and_longitude_validation():
    external_property = ExternalPropertyFactory(gps_latitude="")  # Invalid value
    with pytest.raises(ValidationError):
        external_property.full_clean()


# Source ID
def test_source_id_uniqueness():
    ExternalPropertyFactory(source_id="abc123")
    with pytest.raises(ValidationError):
        property_2 = ExternalPropertyFactory.build(source_id="abc123")
        property_2.full_clean()
