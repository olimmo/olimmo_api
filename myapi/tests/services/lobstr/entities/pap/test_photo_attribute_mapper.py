from myapi.services.lobstr.entities.pap.photo_attribute_mapper import (
    PhotoAttributeMapper,
)

from myapi.tests.factories import ExternalPropertyFactory


class TestPhotoAttributeMapper:
    def test_map_attributes(self):
        external_property = ExternalPropertyFactory()

        pap_property = {
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
            "image_urls": "https://static.pap.fr/photos/E69/E69A0641.jpg, "
            "https://static.pap.fr/photos/E69/E69B0642.jpg, "
            "https://static.pap.fr/photos/E69/E69B0643.jpg, "
            "https://static.pap.fr/photos/E69/E69B0644.jpg",
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

        expected_result = [
            {
                "url": "https://static.pap.fr/photos/E69/E69A0641.jpg",
                "content_object": external_property,
                "position": 1,
            },
            {
                "url": "https://static.pap.fr/photos/E69/E69B0642.jpg",
                "content_object": external_property,
                "position": 2,
            },
            {
                "url": "https://static.pap.fr/photos/E69/E69B0643.jpg",
                "content_object": external_property,
                "position": 3,
            },
            {
                "url": "https://static.pap.fr/photos/E69/E69B0644.jpg",
                "content_object": external_property,
                "position": 4,
            },
        ]

        mapper = PhotoAttributeMapper(pap_property, external_property)
        assert mapper.map_attributes() == expected_result
