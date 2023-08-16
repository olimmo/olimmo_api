import factory
from factory.django import DjangoModelFactory

from .custom_user_factory import CustomUserFactory
from .external_property_factory import ExternalPropertyFactory

from myapi.models import UserExternalProperty


class UserExternalPropertyFactory(DjangoModelFactory):
    class Meta:
        model = UserExternalProperty

    state = factory.Iterator(["contacted", "rejected", "waiting"])

    # Relationships
    external_property = factory.SubFactory(ExternalPropertyFactory)
    user = factory.SubFactory(CustomUserFactory)
