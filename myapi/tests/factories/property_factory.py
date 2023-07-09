import factory
from myapi.models import Property

from .seller_factory import SellerFactory


class PropertyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Property

    address = factory.Faker("address")
    city = factory.Faker("city")
    country = factory.Faker("country")
    postal_code = factory.Faker("zipcode")
    surface = factory.Faker("random_int", min=0, max=100000)
    title = factory.Sequence(lambda n: f"Property {n}")
    seller = factory.SubFactory(SellerFactory)
