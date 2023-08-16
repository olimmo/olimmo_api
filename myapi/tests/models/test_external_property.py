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
def test_city_is_not_blank():
    with pytest.raises(ValidationError, match="cannot be blank."):
        external_property = ExternalPropertyFactory(city="")
        external_property.full_clean()


def test_city_is_not_null():
    with pytest.raises(ValidationError, match="cannot be null."):
        external_property = ExternalPropertyFactory.build(city=None)
        external_property.full_clean()


def test_currency_inclusion():
    with pytest.raises(ValidationError, match="is not a valid choice."):
        external_property = ExternalPropertyFactory(currency="ABC")
        external_property.full_clean()


def test_currency_is_not_blank():
    with pytest.raises(ValidationError, match="cannot be blank."):
        external_property = ExternalPropertyFactory(currency="")
        external_property.full_clean()


def test_currency_is_not_null():
    with pytest.raises(ValidationError, match="cannot be null."):
        external_property = ExternalPropertyFactory.build(currency=None)
        external_property.full_clean()


def test_description_is_not_blank():
    with pytest.raises(ValidationError, match="cannot be blank."):
        external_property = ExternalPropertyFactory(description="")
        external_property.full_clean()


def test_energy_rate_inclusion():
    with pytest.raises(ValidationError, match="is not a valid choice."):
        external_property = ExternalPropertyFactory(energy_rate="K")
        external_property.full_clean()


def test_energy_rate_can_be_none():
    external_property = ExternalPropertyFactory.build(energy_rate=None)
    external_property.clean_and_save()
    assert ExternalProperty.objects.count() == 1


def test_energy_rate_can_be_blank():
    external_property = ExternalPropertyFactory.build(energy_rate="")
    external_property.clean_and_save()
    assert ExternalProperty.objects.count() == 1


def test_first_photo_url_is_not_blank():
    with pytest.raises(ValidationError, match="cannot be blank."):
        external_property = ExternalPropertyFactory(first_photo_url="")
        external_property.full_clean()


def test_first_photo_url_is_not_null():
    with pytest.raises(ValidationError, match="cannot be null."):
        external_property = ExternalPropertyFactory.build(first_photo_url=None)
        external_property.full_clean()


def test_first_photo_url_is_a_url_format():
    with pytest.raises(ValidationError, match="Enter a valid URL."):
        external_property = ExternalPropertyFactory(first_photo_url="not a valid url")
        external_property.full_clean()


def test_floor_number_is_greater_or_equal_than_0():
    with pytest.raises(ValidationError, match="greater than or equal to 0."):
        external_property = ExternalPropertyFactory(floor_number=-1)
        external_property.full_clean()


def test_floor_number_is_less_than_100():
    with pytest.raises(ValidationError, match="less than or equal to 100."):
        external_property = ExternalPropertyFactory(floor_number=101)
        external_property.full_clean()


def test_floor_number_can_be_none():
    external_property = ExternalPropertyFactory.build(floor_number=None)
    external_property.clean_and_save()
    assert ExternalProperty.objects.count() == 1


def test_gps_latitude_is_not_blank():
    with pytest.raises(ValidationError, match="cannot be blank."):
        external_property = ExternalPropertyFactory(gps_latitude="")
        external_property.full_clean()


def test_gps_latitude_is_not_null():
    with pytest.raises(ValidationError, match="cannot be null."):
        external_property = ExternalPropertyFactory.build(gps_latitude=None)
        external_property.full_clean()


def test_gps_latitude_is_not_less_than_20_characters():
    with pytest.raises(ValidationError, match="has at most 20 characters"):
        external_property = ExternalPropertyFactory.build(gps_latitude="1" * 21)
        external_property.full_clean()


def test_gps_longitude_is_not_blank():
    with pytest.raises(ValidationError, match="cannot be blank."):
        external_property = ExternalPropertyFactory(gps_longitude="")
        external_property.full_clean()


def test_gps_longitude_is_not_null():
    with pytest.raises(ValidationError, match="cannot be null."):
        external_property = ExternalPropertyFactory.build(gps_longitude=None)
        external_property.full_clean()


def test_gps_longitude_is_not_less_than_20_characters():
    with pytest.raises(ValidationError, match="has at most 20 characters"):
        external_property = ExternalPropertyFactory.build(gps_longitude="1" * 21)
        external_property.full_clean()


def test_greenhouse_gas_inclusion():
    with pytest.raises(ValidationError, match="is not a valid choice."):
        external_property = ExternalPropertyFactory(greenhouse_gas="K")
        external_property.full_clean()


def test_greenhouse_gas_can_be_none():
    external_property = ExternalPropertyFactory.build(greenhouse_gas=None)
    external_property.clean_and_save()
    assert ExternalProperty.objects.count() == 1


def test_greenhouse_gas_can_be_blank():
    external_property = ExternalPropertyFactory.build(greenhouse_gas="")
    external_property.clean_and_save()
    assert ExternalProperty.objects.count() == 1


def test_nb_floors_building_is_greater_or_equal_than_0():
    with pytest.raises(ValidationError, match="greater than or equal to 0."):
        external_property = ExternalPropertyFactory(nb_floors_building=-1)
        external_property.full_clean()


def test_nb_floors_building_is_less_than_100():
    with pytest.raises(ValidationError, match="less than or equal to 100."):
        external_property = ExternalPropertyFactory(nb_floors_building=101)
        external_property.full_clean()


def test_nb_floors_building_can_be_none():
    external_property = ExternalPropertyFactory.build(nb_floors_building=None)
    external_property.clean_and_save()
    assert ExternalProperty.objects.count() == 1


def test_nb_parkings_is_greater_or_equal_than_0():
    with pytest.raises(ValidationError, match="greater than or equal to 0."):
        external_property = ExternalPropertyFactory(nb_parkings=-1)
        external_property.full_clean()


def test_nb_parkings_is_less_than_100():
    with pytest.raises(ValidationError, match="less than or equal to 100."):
        external_property = ExternalPropertyFactory(nb_parkings=101)
        external_property.full_clean()


def test_nb_parkings_can_be_none():
    external_property = ExternalPropertyFactory.build(nb_parkings=None)
    external_property.clean_and_save()
    assert ExternalProperty.objects.count() == 1


def test_nb_bedrooms_is_greater_or_equal_than_0():
    with pytest.raises(ValidationError, match="greater than or equal to 0."):
        external_property = ExternalPropertyFactory(nb_bedrooms=-1)
        external_property.full_clean()


def test_nb_bedrooms_can_be_none():
    external_property = ExternalPropertyFactory.build(nb_bedrooms=None)
    external_property.clean_and_save()
    assert ExternalProperty.objects.count() == 1


def test_nb_bedrooms_is_less_than_100():
    with pytest.raises(ValidationError, match="less than or equal to 100."):
        external_property = ExternalPropertyFactory(nb_bedrooms=101)
        external_property.full_clean()


def test_nb_rooms_is_greater_or_equal_than_0():
    with pytest.raises(ValidationError, match="greater than or equal to 0."):
        external_property = ExternalPropertyFactory(nb_rooms=-1)
        external_property.full_clean()


def test_nb_rooms_is_not_null():
    with pytest.raises(ValidationError, match="cannot be null."):
        external_property = ExternalPropertyFactory.build(nb_rooms=None)
        external_property.full_clean()


def test_nb_rooms_is_less_than_100():
    with pytest.raises(ValidationError, match="less than or equal to 100."):
        external_property = ExternalPropertyFactory(nb_rooms=101)
        external_property.full_clean()


def test_outside_access_can_be_none():
    external_property = ExternalPropertyFactory.build(outside_access=None)
    external_property.clean_and_save()
    assert ExternalProperty.objects.count() == 1


def test_outside_access_can_be_blank():
    external_property = ExternalPropertyFactory.build(outside_access="")
    external_property.clean_and_save()
    assert ExternalProperty.objects.count() == 1


def test_postal_code_is_not_blank():
    with pytest.raises(ValidationError, match="cannot be blank."):
        external_property = ExternalPropertyFactory(postal_code="")
        external_property.full_clean()


def test_postal_code_is_not_null():
    with pytest.raises(ValidationError, match="cannot be null."):
        external_property = ExternalPropertyFactory.build(postal_code=None)
        external_property.full_clean()


def test_property_type_is_not_blank():
    with pytest.raises(ValidationError, match="cannot be blank."):
        external_property = ExternalPropertyFactory(property_type="")
        external_property.full_clean()


def test_property_type_is_not_null():
    with pytest.raises(ValidationError, match="cannot be null."):
        external_property = ExternalPropertyFactory.build(property_type=None)
        external_property.full_clean()


def test_property_type_inclusion():
    with pytest.raises(ValidationError, match="is not a valid choice."):
        external_property = ExternalPropertyFactory(property_type="Villa")
        external_property.full_clean()


def test_region_is_not_blank():
    with pytest.raises(ValidationError, match="cannot be blank."):
        external_property = ExternalPropertyFactory(region="")
        external_property.full_clean()


def test_seller_phone_can_be_blank():
    external_property = ExternalPropertyFactory.build(seller_phone=None)
    external_property.clean_and_save()
    assert ExternalProperty.objects.count() == 1


def test_seller_name_can_be_blank():
    external_property = ExternalPropertyFactory.build(seller_name=None)
    external_property.clean_and_save()
    assert ExternalProperty.objects.count() == 1


def test_seller_email_is_an_email_format():
    with pytest.raises(ValidationError, match="Enter a valid email address."):
        external_property = ExternalPropertyFactory(seller_email="WrongFormat")
        external_property.full_clean()


def test_seller_email_can_be_blank():
    external_property = ExternalPropertyFactory.build(seller_email=None)
    external_property.clean_and_save()
    assert ExternalProperty.objects.count() == 1


def test_source_not_blank():
    with pytest.raises(ValidationError, match="cannot be blank."):
        external_property = ExternalPropertyFactory(source="")
        external_property.full_clean()


def test_source_is_not_null():
    with pytest.raises(ValidationError, match="cannot be null."):
        external_property = ExternalPropertyFactory.build(source=None)
        external_property.full_clean()


def test_source_inclusion():
    with pytest.raises(ValidationError, match="is not a valid choice."):
        external_property = ExternalPropertyFactory(source="Facebook")
        external_property.full_clean()


def test_source_id_is_not_blank():
    with pytest.raises(ValidationError, match="cannot be blank."):
        external_property = ExternalPropertyFactory(source_id="")
        external_property.full_clean()


def test_source_id_is_not_null():
    with pytest.raises(ValidationError, match="cannot be null."):
        external_property = ExternalPropertyFactory.build(source_id=None)
        external_property.full_clean()


def test_source_id_is_less_than_100_characters():
    with pytest.raises(ValidationError, match="has at most 100 characters"):
        external_property = ExternalPropertyFactory.build(source_id="1" * 101)
        external_property.full_clean()


def test_surface_is_greater_or_equal_than_0():
    with pytest.raises(ValidationError, match="greater than or equal to 0."):
        external_property = ExternalPropertyFactory(surface=-1)
        external_property.full_clean()


def test_surface_is_less_than_100():
    with pytest.raises(ValidationError, match="less than or equal to 10000."):
        external_property = ExternalPropertyFactory(surface=10001)
        external_property.full_clean()


def test_surface_is_not_null():
    with pytest.raises(ValidationError, match="cannot be null."):
        external_property = ExternalPropertyFactory.build(surface=None)
        external_property.full_clean()


def test_title_is_not_blank():
    with pytest.raises(ValidationError, match="cannot be blank."):
        external_property = ExternalPropertyFactory(title="")
        external_property.full_clean()


def test_title_is_not_null():
    with pytest.raises(ValidationError, match="cannot be null."):
        external_property = ExternalPropertyFactory.build(title=None)
        external_property.full_clean()


def test_url_is_not_null():
    with pytest.raises(ValidationError, match="cannot be null."):
        external_property = ExternalPropertyFactory.build(url=None)
        external_property.full_clean()


def test_url_is_not_blank():
    with pytest.raises(ValidationError, match="cannot be blank."):
        external_property = ExternalPropertyFactory(url="")
        external_property.full_clean()


def test_url_is_a_url_format():
    with pytest.raises(ValidationError, match="Enter a valid URL."):
        external_property = ExternalPropertyFactory(url="not a valid url")
        external_property.full_clean()
