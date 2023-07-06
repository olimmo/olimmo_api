import factory
from myapi.models import Property


class PropertyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Property

    city = factory.Faker('city')
    surface = factory.Faker('random_int', min=0, max=100000)
    title = factory.Faker('sentence', nb_words=4)
