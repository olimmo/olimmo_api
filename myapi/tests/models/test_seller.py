import pytest
from myapi.tests.factories import SellerFactory
from myapi.models import Seller
from django.core.exceptions import ValidationError


# Test the creation of a Seller instance
def test_seller_creation():
    SellerFactory()
    assert Seller.objects.count() == 1


# Test the string representation of the Seller model
def test_seller_str_representation():
    seller = SellerFactory()
    assert str(seller) == str(vars(seller))


# Test the email validators
def test_seller_email_validators():
    # Test email with zero characters
    with pytest.raises(ValidationError):
        seller = SellerFactory.build(email="")
        seller.full_clean()

    # Test unique email constraint
    SellerFactory(email="test@example.com")
    with pytest.raises(ValidationError):
        seller = SellerFactory.build(email="test@example.com")
        seller.full_clean()


# Test the first_name validators
def test_seller_first_name_validators():
    # Test first_name with zero characters
    with pytest.raises(ValidationError):
        seller = SellerFactory.build(first_name="")
        seller.full_clean()


# Test the last_name validators
def test_seller_last_name_validators():
    # Test last_name with zero characters
    with pytest.raises(ValidationError):
        seller = SellerFactory.build(last_name="")
        seller.full_clean()


# Test the phone validators
def test_seller_phone_validators():
    # Test phone with zero characters
    with pytest.raises(ValidationError):
        seller = SellerFactory.build(phone="")
        seller.full_clean()
