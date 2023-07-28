# factories.py
import factory
from factory.fuzzy import FuzzyInteger, FuzzyChoice
from myapi.models import ExternalProperty


class ExternalPropertyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ExternalProperty

    title = factory.Faker("sentence")
    surface = FuzzyInteger(0, 100000)
    city = factory.Faker("city")
    currency = FuzzyChoice(["EUR", "USD"])
    description = factory.Faker("paragraph")
    elevator = factory.Faker("boolean")
    energy_rate = factory.Faker("word")
    first_photo_url = factory.Sequence(lambda n: f"https://www.{n}.com")
    floor_number = FuzzyInteger(0, 100000)
    gps_latitude = factory.Faker("latitude")
    gps_longitude = factory.Faker("longitude")
    greenhouse_gas = factory.Faker("word")
    has_phone = factory.Faker("boolean")
    immo_type = factory.Faker("word")
    kind = factory.Faker("word")
    nb_floors_building = FuzzyInteger(0, 100000)
    nb_parkings = FuzzyInteger(0, 100000)
    nb_rooms = FuzzyInteger(0, 100)
    outside_access = factory.Faker("word")
    postal_code = factory.Faker("postcode")
    region = factory.Faker("state")
    source = FuzzyChoice(["Leboncoin", "PAP"])
    source_id = factory.Sequence(lambda n: f"Source {n}")
    url = factory.Sequence(lambda n: f"https://www.{n}.com")
