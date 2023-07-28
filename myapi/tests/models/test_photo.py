import pytest
from myapi.models import Photo
from django.core.exceptions import ValidationError
from myapi.tests.factories import PhotoFactory


@pytest.fixture
def photo():
    return PhotoFactory()


# Creation
def test_photo_creation(photo):
    assert isinstance(photo, Photo)
    assert photo.id is not None
    assert photo.position is not None
    assert photo.url is not None


# Validationsx
def test_position_validation():
    with pytest.raises(ValidationError):
        photo = PhotoFactory(position=-1)  # Invalid value
        photo.full_clean()

    with pytest.raises(ValidationError):
        photo = PhotoFactory(position=100001)  # Invalid value
        photo.full_clean()


def test_url_validation():
    with pytest.raises(ValidationError):
        photo = PhotoFactory(url="not a valid url")  # Invalid URL
        photo.full_clean()


def test_photo_has_external_property():
    photo = PhotoFactory()
    assert photo.external_property is not None
