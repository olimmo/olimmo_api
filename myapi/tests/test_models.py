# your_app/tests/test_models.py
import pytest
from .factories import PropertyFactory


@pytest.mark.django_db
def test_property_creation():
    property = PropertyFactory()
    assert property.title is not None
    assert property.city is not None
    assert 0 <= property.surface <= 100000
