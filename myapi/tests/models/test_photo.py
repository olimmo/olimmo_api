import pytest
from myapi.models import Photo
from django.core.exceptions import ValidationError
from myapi.tests.factories import PhotoFactory


@pytest.fixture
def photo():
    return PhotoFactory()


def test_photo_creation(photo):
    assert isinstance(photo, Photo)
    assert photo.id is not None
    assert photo.position is not None
    assert photo.url is not None


def test_position_is_greater_or_equal_to_0():
    with pytest.raises(ValidationError, match="greater than or equal to 1."):
        photo = PhotoFactory(position=-1)
        photo.full_clean()


def test_postion_is_less_than_1000():
    with pytest.raises(ValidationError, match="less than or equal to 1000."):
        photo = PhotoFactory(position=1001)
        photo.full_clean()


def test_position_is_not_null():
    with pytest.raises(ValidationError, match="cannot be null."):
        photo = PhotoFactory.build(position=None)
        photo.full_clean()


def test_url_is_not_null():
    with pytest.raises(ValidationError, match="cannot be null."):
        external_property = PhotoFactory.build(url=None)
        external_property.full_clean()


def test_url_is_not_blank():
    with pytest.raises(ValidationError, match="cannot be blank."):
        photo = PhotoFactory(url="")
        photo.full_clean()


def test_url_is_a_url_format():
    with pytest.raises(ValidationError, match="Enter a valid URL."):
        photo = PhotoFactory(url="not a valid url")
        photo.full_clean()


def test_photo_has_external_property():
    photo = PhotoFactory()
    assert photo.external_property is not None
