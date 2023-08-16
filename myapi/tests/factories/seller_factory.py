import factory
from factory.django import DjangoModelFactory

from myapi.models import Seller


class SellerFactory(DjangoModelFactory):
    class Meta:
        model = Seller

    civility = factory.Iterator(["mr", "mrs", "unspecified"])
    email = factory.Sequence(lambda n: f"seller{n}@example.com")
    first_name = "John"
    last_name = "Doe"
    phone = "+33612345678"
