# test_tasks.py

from unittest.mock import patch
from django.contrib.contenttypes.models import ContentType

from myapi.tasks.lobstr.leboncoin.external_property_create_task import (
    create_external_property_task,
)
from myapi.models import ExternalProperty, Photo


class TestExternalPropertyCreateTask:
    leboncoin_properties = [
        {
            "id": "ce49cda8afad013d3f4391d360844420",
            "DPE_string": "D",
            "GES_string": "C",
            "annonce_id": "2387017657",
            "api_key": "54bb0281238b45a03f0ee695f73e704f",
            "area": 13,
            "capacity": None,
            "category_name": "Ventes immobilières",
            "city": "Paris 75014 14e Arrondissement",
            "currency": "EUR",
            "department": "Paris",
            "description": "Studio tout confort ...",
            "floor": None,
            "has_phone": False,
            "lat": "48.83292",
            "lng": "2.3248",
            "mail": None,
            "more_details": {
                "ges": "C",
                "rooms": "1",
                "square": "13 m²",
                "is_import": "False",
                "lease_type": "sell",
                "energy_rate": "D",
                "floor_number": "2",
                "outside_access": "Garden",
                "nb_parkings": "0",
                "immo_sell_type": "old",
                "real_estate_type": "Appartement",
                "nb_floors_building": "5",
                "profile_picture_url": "https://img.leboncoin.fr/api/v1/1",
                "type_real_estate_sale": "Ancien",
            },
            "owner_name": "Sorgue",
            "phone": None,
            "picture": None,
            "pictures": "https://img1.jpg|||https://img2.jpg",
            "postal_code": "75014",
            "price": 165000,
            "real_estate_type": "Appartement",
            "region": "Ile-de-France",
            "room_count": 1,
            "sleepingroom_count": None,
            "title": "Studio tout confort 10 min à pied de Montparnasse",
            "url": "https://www.leboncoin.fr/ventes_immobilieres/2387017657.htm",
        }
    ]

    # Create exernal property
    @patch(
        "myapi.services.lobstr.lobstr_property_fetcher.LobstrPropertyFetcher.get_properties"
    )
    def test_external_property_create_task(self, mock_get_properties, db):
        mock_get_properties.return_value = self.leboncoin_properties
        create_external_property_task("run_id")

        assert (
            ExternalProperty.objects.filter(
                currency=self.leboncoin_properties[0]["currency"],
                city=self.leboncoin_properties[0]["department"],
                description=self.leboncoin_properties[0]["description"],
                elevator=False,
                energy_rate=self.leboncoin_properties[0]["DPE_string"],
                first_photo_url=self.leboncoin_properties[0]["more_details"][
                    "profile_picture_url"
                ],
                floor_number=self.leboncoin_properties[0]["more_details"][
                    "floor_number"
                ],
                gps_latitude=self.leboncoin_properties[0]["lat"],
                gps_longitude=self.leboncoin_properties[0]["lng"],
                greenhouse_gas=self.leboncoin_properties[0]["GES_string"],
                nb_bedrooms=self.leboncoin_properties[0]["sleepingroom_count"],
                nb_floors_building=self.leboncoin_properties[0]["more_details"][
                    "nb_floors_building"
                ],
                nb_parkings=self.leboncoin_properties[0]["more_details"]["nb_parkings"],
                nb_rooms=self.leboncoin_properties[0]["more_details"]["rooms"],
                outside_access=self.leboncoin_properties[0]["more_details"][
                    "outside_access"
                ],
                postal_code=self.leboncoin_properties[0]["postal_code"],
                price=self.leboncoin_properties[0]["price"],
                property_type=self.leboncoin_properties[0]["more_details"][
                    "real_estate_type"
                ],
                region=self.leboncoin_properties[0]["region"],
                seller_email=self.leboncoin_properties[0]["mail"],
                seller_name=self.leboncoin_properties[0]["owner_name"],
                seller_phone=self.leboncoin_properties[0]["phone"],
                source="Leboncoin",
                source_id=self.leboncoin_properties[0]["annonce_id"],
                surface=self.leboncoin_properties[0]["area"],
                title=self.leboncoin_properties[0]["title"],
                url=self.leboncoin_properties[0]["url"],
            ).count()
            == 1
        )

    # Create photos
    @patch(
        "myapi.services.lobstr.lobstr_property_fetcher.LobstrPropertyFetcher.get_properties"
    )
    def test_create_photos(self, mock_get_properties, db):
        mock_get_properties.return_value = self.leboncoin_properties
        create_external_property_task("run_id")

        external_property = ExternalProperty.objects.first()
        external_property_content_type = ContentType.objects.get_for_model(
            ExternalProperty
        )
        photos = Photo.objects.filter(
            content_type=external_property_content_type, object_id=external_property.id
        )
        assert photos.count() == 2
        assert photos[0].url == "https://img1.jpg"
        assert photos[1].url == "https://img2.jpg"

    # Whithout lebcoin properties
    @patch(
        "myapi.services.lobstr.lobstr_property_fetcher.LobstrPropertyFetcher.get_properties"
    )
    def test_external_property_create_task_no_properties(self, mock_get_properties, db):
        mock_get_properties.return_value = None
        result = create_external_property_task("run_id")

        assert result is None
        assert ExternalProperty.objects.count() == 0
        assert Photo.objects.count() == 0
