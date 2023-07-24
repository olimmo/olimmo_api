from django.urls import reverse
from rest_framework.test import APITestCase
from myapi.tests.factories import PropertyFactory, SellerFactory
from myapi.models import Property


class PropertyListViewTest(APITestCase):
    def setUp(self):
        self.seller = SellerFactory.create()
        self.property = PropertyFactory.create(seller=self.seller)

    def test_get_properties(self):
        response = self.client.get(
            reverse("seller-properties-list", kwargs={"seller_id": self.seller.id})
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), Property.objects.count())

    def test_post_property(self):
        data = {
            "city": "London",
            "surface": 5000,
            "title": "New Property",
        }
        response = self.client.post(
            reverse("seller-properties-list", kwargs={"seller_id": self.seller.id}),
            data,
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Property.objects.last().title, "New Property")


class PropertyDetailTest(APITestCase):
    def setUp(self):
        self.seller = SellerFactory.create()
        self.property = PropertyFactory.create(seller=self.seller)

    def test_get_property(self):
        response = self.client.get(
            reverse(
                "seller-property-detail",
                kwargs={"seller_id": self.seller.id, "property_id": self.property.id},
            )
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["title"], self.property.title)

    def test_put_property(self):
        data = {
            "location": "Paris",
            "price": 6000,
            "title": "Updated Property",
        }
        response = self.client.put(
            reverse(
                "seller-property-detail",
                kwargs={"seller_id": self.seller.id, "property_id": self.property.id},
            ),
            data,
        )
        self.assertEqual(response.status_code, 200)
        self.property.refresh_from_db()
        self.assertEqual(self.property.title, "Updated Property")

    def test_delete_property(self):
        response = self.client.delete(
            reverse(
                "seller-property-detail",
                kwargs={"seller_id": self.seller.id, "property_id": self.property.id},
            )
        )
        self.assertEqual(response.status_code, 204)
        self.assertFalse(Property.objects.filter(pk=self.property.pk).exists())
