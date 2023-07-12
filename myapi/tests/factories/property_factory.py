import factory
from myapi.models import Property

from .seller_factory import SellerFactory


class PropertyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Property

    address = factory.Sequence(lambda n: f"Address {n}")
    city = factory.Sequence(lambda n: f"City {n}")
    country = factory.Sequence(lambda n: f"Country {n}")
    postal_code = factory.Sequence(lambda n: f"Code {n}")
    surface = factory.Faker("random_int", min=0, max=100000)
    title = factory.Sequence(lambda n: f"Property {n}")
    seller = factory.SubFactory(SellerFactory)
