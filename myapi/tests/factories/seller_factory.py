import factory
from myapi.models import Seller


class SellerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Seller

    civility = factory.Iterator(["mr", "mrs", "unspecified"])
    email = "John.doe@gmail.com"
    first_name = "John"
    last_name = "Doe"
    phone = "+33612345678"
