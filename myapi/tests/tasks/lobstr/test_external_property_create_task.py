# test_tasks.py

from unittest.mock import patch
from django.contrib.contenttypes.models import ContentType

from myapi.tasks.lobstr.external_property_create_task import (
    create_external_property_task,
)
from myapi.models import ExternalProperty, Photo


# Test also for PAP
class TestExternalPropertyCreateTask:
    leboncoin_results = [
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

    @patch(
        "myapi.services.lobstr.lobstr_property_fetcher.LobstrPropertyFetcher.get_properties"
    )
    def test_create_external_property_with_leboncoin_results(
        self, mock_get_properties, db
    ):
        mock_get_properties.return_value = self.leboncoin_results
        create_external_property_task("run_id", "Leboncoin")

        assert (
            ExternalProperty.objects.filter(
                currency=self.leboncoin_results[0]["currency"],
                city=self.leboncoin_results[0]["department"],
                description=self.leboncoin_results[0]["description"],
                elevator=False,
                energy_rate=self.leboncoin_results[0]["DPE_string"],
                first_photo_url=self.leboncoin_results[0]["pictures"].split("|||")[0],
                floor_number=self.leboncoin_results[0]["more_details"]["floor_number"],
                gps_latitude=self.leboncoin_results[0]["lat"],
                gps_longitude=self.leboncoin_results[0]["lng"],
                greenhouse_gas=self.leboncoin_results[0]["GES_string"],
                nb_bedrooms=self.leboncoin_results[0]["sleepingroom_count"],
                nb_floors_building=self.leboncoin_results[0]["more_details"][
                    "nb_floors_building"
                ],
                nb_parkings=self.leboncoin_results[0]["more_details"]["nb_parkings"],
                nb_rooms=self.leboncoin_results[0]["more_details"]["rooms"],
                outside_access=self.leboncoin_results[0]["more_details"][
                    "outside_access"
                ],
                postal_code=self.leboncoin_results[0]["postal_code"],
                price=self.leboncoin_results[0]["price"],
                property_type=self.leboncoin_results[0]["more_details"][
                    "real_estate_type"
                ],
                region=self.leboncoin_results[0]["region"],
                seller_email=self.leboncoin_results[0]["mail"],
                seller_name=self.leboncoin_results[0]["owner_name"],
                seller_phone=self.leboncoin_results[0]["phone"],
                source="Leboncoin",
                source_id=self.leboncoin_results[0]["annonce_id"],
                surface=self.leboncoin_results[0]["area"],
                title=self.leboncoin_results[0]["title"],
                url=self.leboncoin_results[0]["url"],
            ).count()
            == 1
        )

    @patch(
        "myapi.services.lobstr.lobstr_property_fetcher.LobstrPropertyFetcher.get_properties"
    )
    def test_create_photos_with_leboncoin_results(self, mock_get_properties, db):
        mock_get_properties.return_value = self.leboncoin_results
        create_external_property_task("run_id", "Leboncoin")

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

    pap_results = [
        {
            "id": "0207283b7085c40e871a94a10d91fa2f",
            "object": "result",
            "run": "9729580b34b74b1d9ba43f59b9fdcf4d",
            "bedrooms": 3,
            "breadcrumb": "Vente Appartement/ Vente Appartement Paris 14e",
            "currency": "euro",
            "description": "Quartier Pernety. A 300 mètres du métro à pied...",
            "energy": "D",
            "filling_details": None,
            "ges": "A",
            "image_urls": "https://img1.jpg, https://img2.jpg, https://img3.jpg",
            "internal_id": "446900645",
            "lat": "48.834989",
            "lng": "2.314851",
            "neighborhood": "Paris 14e (75014)",
            "phone": "07.81.28.90.31",
            "price": 730000,
            "publication_date": "2023-08-23T00:00:00Z",
            "ref": "E69/0645",
            "rooms": 4,
            "scraping_time": "2023-08-23T09:35:17.098Z",
            "size": 75,
            "title": "Vente appartement 4 pièces 75 m² Paris 14E (75014)",
            "url": "https://www.pap.fr/annonces/appartement-paris-14e-75014-r446900645",
        }
    ]

    @patch(
        "myapi.services.lobstr.lobstr_property_fetcher.LobstrPropertyFetcher.get_properties"
    )
    def test_create_external_property_with_pap_results(self, mock_get_properties, db):
        mock_get_properties.return_value = self.pap_results
        create_external_property_task("run_id", "PAP")

        assert (
            ExternalProperty.objects.filter(
                currency="EUR",
                city="Paris 14e",
                description=self.pap_results[0]["description"],
                elevator=False,
                energy_rate=self.pap_results[0]["energy"],
                first_photo_url=self.pap_results[0]["image_urls"].split(",")[0],
                floor_number=None,
                gps_latitude=self.pap_results[0]["lat"],
                gps_longitude=self.pap_results[0]["lng"],
                greenhouse_gas=self.pap_results[0]["ges"],
                nb_bedrooms=self.pap_results[0]["bedrooms"],
                nb_floors_building=None,
                nb_parkings=None,
                nb_rooms=self.pap_results[0]["rooms"],
                outside_access=None,
                postal_code="75014",
                price=self.pap_results[0]["price"],
                property_type="Appartement",
                region=None,
                seller_email=None,
                seller_name=None,
                seller_phone="0781289031",
                source="pap",
                source_id=self.pap_results[0]["internal_id"],
                surface=self.pap_results[0]["size"],
                title=self.pap_results[0]["title"],
                url=self.pap_results[0]["url"],
            ).count()
            == 1
        )

    @patch(
        "myapi.services.lobstr.lobstr_property_fetcher.LobstrPropertyFetcher.get_properties"
    )
    def test_create_photos_with_pap_results(self, mock_get_properties, db):
        mock_get_properties.return_value = self.pap_results
        create_external_property_task("run_id", "PAP")

        external_property = ExternalProperty.objects.first()
        external_property_content_type = ContentType.objects.get_for_model(
            ExternalProperty
        )
        photos = Photo.objects.filter(
            content_type=external_property_content_type, object_id=external_property.id
        )
        assert photos.count() == 3
        assert photos[0].url == "https://img1.jpg"
        assert photos[1].url == "https://img2.jpg"
        assert photos[2].url == "https://img3.jpg"

    @patch(
        "myapi.services.lobstr.lobstr_property_fetcher.LobstrPropertyFetcher.get_properties"
    )
    def test_when_the_LobstrPropertyFetcher_does_returns_property(
        self, mock_get_properties, db
    ):
        mock_get_properties.return_value = None
        result = create_external_property_task("run_id", "Leboncoin")

        assert result is None
        assert ExternalProperty.objects.count() == 0
        assert Photo.objects.count() == 0
