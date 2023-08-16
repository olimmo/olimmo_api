import factory
from factory.django import DjangoModelFactory

from myapi.models import CustomUser


class CustomUserFactory(DjangoModelFactory):
    class Meta:
        model = CustomUser

    email = factory.Sequence(lambda n: f"user{n}@example.com")
    password = factory.PostGenerationMethodCall("set_password", "default_password")
    is_staff = factory.Faker("boolean")
