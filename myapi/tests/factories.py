import factory
from myapi.models import Property


class PropertyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Property

    address = factory.Faker("street_address")
    city = factory.Faker("city")
    postal_code = factory.Faker("postcode")
    country = factory.Faker("country")
    surface = factory.Faker("random_int", min=0, max=100000)
    title = factory.Faker("sentence", nb_words=4)
