import pytest
from myapi.models import Seller
from myapi.tests.factories import SellerFactory


@pytest.fixture
def seller():
    return SellerFactory()


def test_seller_creation(seller):
    assert isinstance(seller, Seller)
    assert seller.id is not None
    assert seller.email is not None
    assert seller.phone is not None
    assert seller.first_name is not None
    assert seller.last_name is not None


def test_seller_attributes():
    seller = SellerFactory(civility="mr", email="john@example.com")

    assert seller.civility == "mr"
    assert seller.email == "john@example.com"
    # Add additional assertions as needed
