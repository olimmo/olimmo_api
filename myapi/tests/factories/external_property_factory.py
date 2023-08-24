# factories.py
import factory
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyInteger, FuzzyChoice

from myapi.models import ExternalProperty


class ExternalPropertyFactory(DjangoModelFactory):
    class Meta:
        model = ExternalProperty

    title = factory.Faker("sentence")
    surface = FuzzyInteger(0, 10000)
    city = factory.Faker("city")
    currency = FuzzyChoice(["EUR", "USD"])
    description = factory.Faker("paragraph")
    elevator = factory.Faker("boolean")
    energy_rate = FuzzyChoice(["A", "B", "C", "D", "E", "F", "G"])
    first_photo_url = factory.Sequence(
        lambda n: f"https://picsum.photos/id/{n}/200/300"
    )
    floor_number = FuzzyInteger(0, 100)
    gps_latitude = factory.Faker("latitude")
    gps_longitude = factory.Faker("longitude")
    greenhouse_gas = FuzzyChoice(["A", "B", "C", "D", "E", "F", "G"])
    nb_bedrooms = FuzzyInteger(0, 10)
    nb_floors_building = FuzzyInteger(0, 30)
    nb_parkings = FuzzyInteger(0, 10)
    nb_rooms = FuzzyInteger(0, 15)
    outside_access = factory.Faker("word")
    postal_code = factory.Faker("postcode")
    price = FuzzyInteger(100000, 5000000)
    property_type = FuzzyChoice(["Appartement", "House"])
    region = factory.Faker("state")
    seller_email = factory.Faker("email")
    seller_name = factory.Faker("word")
    seller_phone = factory.Faker("phone_number")
    source = FuzzyChoice(["leboncoin", "pap"])
    source_id = factory.Sequence(lambda n: f"Source {n}")
    url = factory.Sequence(lambda n: f"https://www.{n}.com")
