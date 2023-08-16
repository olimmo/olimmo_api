from myapi.models import UserExternalProperty
from myapi.tests.factories import CustomUserFactory, ExternalPropertyFactory


def test_create_user_external_property_signal():
    # Create a test user
    user = CustomUserFactory()

    # Ensure no UserExternalProperty instances exist before our test
    assert UserExternalProperty.objects.count() == 0

    # Create an ExternalProperty, which should trigger the signal
    property_instance = ExternalPropertyFactory()

    # Check if a UserExternalProperty instance was created
    assert UserExternalProperty.objects.count() == 1

    user_property = UserExternalProperty.objects.first()
    assert user_property.user == user
    assert user_property.external_property == property_instance
