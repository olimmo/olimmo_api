import pytest

from myapi.tests.factories import CustomUserFactory

from myapi.models import CustomUser


@pytest.mark.django_db
def test_custom_user_creation():
    user = CustomUserFactory()

    assert CustomUser.objects.filter(email=user.email).exists()

    # Check if the user's email is correctly set
    assert user.email == user.email

    # Check if the user's password is correctly set
    assert user.check_password("default_password")

    # Check if the user's is_staff attribute is correctly set
    assert isinstance(user.is_staff, bool)
