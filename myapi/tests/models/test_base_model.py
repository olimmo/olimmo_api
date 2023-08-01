# tests/test_base_model.py

import pytest
from django.core.exceptions import ValidationError
from myapi.models import ExternalProperty
from myapi.tests.factories import ExternalPropertyFactory


def test_clean_and_save_with_valid_instance():
    instance = ExternalPropertyFactory.build()

    instance.clean_and_save()
    assert ExternalProperty.objects.filter(title=instance.title).count() == 1


def test_clean_and_save_with_invalid_instance():
    instance = ExternalPropertyFactory.build(title="")

    with pytest.raises(ValidationError):
        instance.clean_and_save()
    assert ExternalProperty.objects.count() == 0
