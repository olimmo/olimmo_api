import factory
from myapi.models import Photo

from .external_property_factory import ExternalPropertyFactory


class PhotoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Photo

    position = factory.Faker("random_int", min=0, max=1000)
    url = factory.Sequence(lambda n: f"https://www.{n}.com")

    external_property = factory.SubFactory(ExternalPropertyFactory)
