import factory
from factory.django import DjangoModelFactory

from django.contrib.contenttypes.models import ContentType

from .external_property_factory import ExternalPropertyFactory

from myapi.models import Photo


class PhotoFactory(DjangoModelFactory):
    class Meta:
        model = Photo

    position = factory.Faker("random_int", min=0, max=1000)
    url = factory.Sequence(lambda n: f"https://picsum.photos/id/{n}/200/300")

    content_type = factory.LazyAttribute(
        lambda o: ContentType.objects.get_for_model(o.content_object)
    )
    object_id = factory.SelfAttribute("content_object.pk")
    content_object = factory.SubFactory(ExternalPropertyFactory)
