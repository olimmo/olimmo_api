from myapi.services.lobstr.entities.leboncoin.photo_attribute_mapper import (
    PhotoAttributeMapper,
)

from myapi.tests.factories import ExternalPropertyFactory


class TestPhotoAttributeMapper:
    def test_map_attributes(self):
        external_property = ExternalPropertyFactory()

        leboncoin_property = {
            "currency": "EUR",
            "department": "Paris",
            "description": "Nice apartment",
            "DPE_string": "D",
            "GES_string": "C",
            "lat": "48.8566",
            "lng": "2.3522",
            "mail": "test@example.com",
            "owner_name": "Owner",
            "phone": "0123456789",
            "postal_code": "75000",
            "region": "Île-de-France",
            "annonce_id": "12345",
            "area": 100,
            "title": "Apartment for sale",
            "url": "http://example.com",
            "pictures": "https://img.leboncoin.fr/api/v1/lbcpb1/images/c1.jpg|||"
            "https://img.leboncoin.fr/api/v1/lbcpb1/images/c2.jpg|||"
            "https://img.leboncoin.fr/api/v1/lbcpb1/images/c3.jpg|||"
            "https://img.leboncoin.fr/api/v1/lbcpb1/images/c4.jpg",
            "price": 500000,
            "more_details": {
                "elevator": "Oui",
                "profile_picture_url": "http://example.com/photo.jpg",
                "floor_number": "2",
                "sleepingroom_count": "2",
                "nb_floors_building": "5",
                "nb_parkings": "1",
                "rooms": "3",
                "outside_access": "Garden",
                "real_estate_type": "Apartment",
            },
        }

        expected_result = [
            {
                "url": "https://img.leboncoin.fr/api/v1/lbcpb1/images/c1.jpg",
                "content_object": external_property,
                "position": 1,
            },
            {
                "url": "https://img.leboncoin.fr/api/v1/lbcpb1/images/c2.jpg",
                "content_object": external_property,
                "position": 2,
            },
            {
                "url": "https://img.leboncoin.fr/api/v1/lbcpb1/images/c3.jpg",
                "content_object": external_property,
                "position": 3,
            },
            {
                "url": "https://img.leboncoin.fr/api/v1/lbcpb1/images/c4.jpg",
                "content_object": external_property,
                "position": 4,
            },
        ]

        mapper = PhotoAttributeMapper(leboncoin_property, external_property)
        assert mapper.map_attributes() == expected_result
