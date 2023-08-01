from myapi.services.lobstr.entities.leboncoin_property_attribute_mapper import (
    LeBonCoinPropertyAttributeMapper,
)


class TestLeBonCoinPropertyAttributeMapper:
    def test_map_attributes(self):
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
        expected_result = {
            "currency": "EUR",
            "city": "Paris",
            "description": "Nice apartment",
            "elevator": True,
            "energy_rate": "D",
            "first_photo_url": "http://example.com/photo.jpg",
            "floor_number": 2,
            "gps_latitude": "48.8566",
            "gps_longitude": "2.3522",
            "greenhouse_gas": "C",
            "nb_bedrooms": 2,
            "nb_floors_building": 5,
            "nb_parkings": 1,
            "nb_rooms": 3,
            "outside_access": "Garden",
            "postal_code": "75000",
            "price": 500000,
            "property_type": "Apartment",
            "region": "Île-de-France",
            "seller_email": "test@example.com",
            "seller_name": "Owner",
            "seller_phone": "0123456789",
            "source": "Leboncoin",
            "source_id": "12345",
            "surface": 100,
            "title": "Apartment for sale",
            "url": "http://example.com",
        }

        mapper = LeBonCoinPropertyAttributeMapper(leboncoin_property)
        assert mapper.map_attributes() == expected_result
