import factory
from django.contrib.contenttypes.models import ContentType

from myapi.models import Photo

from .external_property_factory import ExternalPropertyFactory


class PhotoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Photo

    position = factory.Faker("random_int", min=0, max=1000)
    url = factory.Sequence(lambda n: f"https://www.{n}.com")

    content_type = factory.LazyAttribute(
        lambda o: ContentType.objects.get_for_model(o.content_object)
    )
    object_id = factory.SelfAttribute("content_object.pk")
    content_object = factory.SubFactory(ExternalPropertyFactory)
