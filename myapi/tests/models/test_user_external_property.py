import pytest
from myapi.models import UserExternalProperty
from django.core.exceptions import ValidationError
from myapi.tests.factories import UserExternalPropertyFactory


@pytest.fixture
def user_external_property():
    return UserExternalPropertyFactory()


# Creation
def test_user_external_property_creation(user_external_property):
    assert isinstance(user_external_property, UserExternalProperty)
    assert user_external_property.id is not None
    assert user_external_property.state is not None
    assert user_external_property.user_id is not None
    assert user_external_property.external_property_id is not None


# Validations
def test_user_id_is_not_null():
    with pytest.raises(ValidationError, match="cannot be null."):
        user_external_property = UserExternalPropertyFactory.build(user_id=None)
        user_external_property.full_clean()


def test_external_property_is_not_null():
    with pytest.raises(ValidationError, match="cannot be null."):
        user_external_property = UserExternalPropertyFactory.build(
            external_property=None
        )
        user_external_property.full_clean()


def test_user_id_and_external_property_is_uniq_together():
    exiting_user_external_property = UserExternalPropertyFactory()
    with pytest.raises(
        ValidationError,
        match="User external property with this User and External property already exists.",
    ):
        new_user_external_property = UserExternalPropertyFactory.build(
            user=exiting_user_external_property.user,
            external_property=exiting_user_external_property.external_property,
        )
        new_user_external_property.clean_and_save()


def test_state_inclusion():
    with pytest.raises(ValidationError, match="is not a valid choice."):
        user_external_property = UserExternalPropertyFactory(state="WrongState")
        user_external_property.full_clean()
