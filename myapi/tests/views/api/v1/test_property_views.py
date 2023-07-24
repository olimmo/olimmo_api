from django.urls import reverse
from rest_framework.test import APITestCase
from myapi.tests.factories import PropertyFactory
from myapi.models import Property


class PropertyListViewTest(APITestCase):
    def setUp(self):
        self.property = PropertyFactory.create()

    def test_get_properties(self):
        response = self.client.get(reverse("property-list"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), Property.objects.count())

    def test_post_property(self):
        data = {
            "city": "London",
            "postal_code": "1234567890",
            "surface": 5000,
            "title": "New Property",
        }
        response = self.client.post(reverse("property-list"), data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Property.objects.last().title, "New Property")


class PropertyDetailTest(APITestCase):
    def setUp(self):
        self.property = PropertyFactory.create()

    def test_get_property(self):
        response = self.client.get(
            reverse("property-detail", kwargs={"pk": self.property.pk})
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["title"], self.property.title)

    def test_put_property(self):
        data = {
            "location": "Paris",
            "postal_code": "1223",
            "price": 6000,
            "title": "Updated Property",
        }
        response = self.client.put(
            reverse("property-detail", kwargs={"pk": self.property.pk}), data
        )
        self.assertEqual(response.status_code, 200)
        self.property.refresh_from_db()
        self.assertEqual(self.property.title, "Updated Property")

    def test_delete_property(self):
        response = self.client.delete(
            reverse("property-detail", kwargs={"pk": self.property.pk})
        )
        self.assertEqual(response.status_code, 204)
        self.assertFalse(Property.objects.filter(pk=self.property.pk).exists())
