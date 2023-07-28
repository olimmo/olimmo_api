from django.urls import reverse
from rest_framework.test import APITestCase
from myapi.tests.factories import PropertyFactory
from myapi.models import Property


class ExternalPropertyListViewTest(APITestCase):
    def setUp(self):
        self.property = PropertyFactory.create()

    def test_post_property(self):
        data = {
            "title": "New Property",
            "address": "12 rue de la paix",
            "city": "London",
            "country": "UK",
            "surface": 1001,
            "postal_code": "883833",
            "currency": "EUR",
            "description": "Test from example",
            "region": "Ile de france",
            "source": "leBoncoin",
            "source_id": "jejejejh",
            "url": "https://www.ejejej.com",
        }
        response = self.client.post(reverse("property-list"), data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Property.objects.last().title, "New Property")
