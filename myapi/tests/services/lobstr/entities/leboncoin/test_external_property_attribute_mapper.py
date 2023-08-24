from myapi.services.lobstr.entities.leboncoin.external_property_attribute_mapper import (
    ExternalPropertyAttributeMapper,
)


class TestExternalPropertyAttributeMapper:
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
            "pictures": "https://img.leboncoin.fr/api/v1/lbcpb1/images/c9/1f/16/c91f16bf2ce8515df0"
            "5f6de50475c429b683657f.jpg?rule=ad-large|||https://img.leboncoin.fr/api/v1/lbcpb1/im"
            "ages/01/ce/5e/01ce5e4e4cb9e6f9d850bb7be00118f99f8784f7.jpg?rule=ad-large|||"
            "https://img.leboncoin.fr/api/v1/lbcpb1/images/da/be/17/dabe173e8c33259e74fba3e0da"
            "debb359629bbeb.jpg?rule=ad-large",
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
            "first_photo_url": "https://img.leboncoin.fr/api/v1/lbcpb1/images/c9/1f/16/c91f16bf2c"
            "e8515df05f6de50475c429b683657f.jpg?rule=ad-large",
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
            "source": "leboncoin",
            "source_id": "12345",
            "surface": 100,
            "title": "Apartment for sale",
            "url": "http://example.com",
        }

        mapper = ExternalPropertyAttributeMapper(leboncoin_property)
        assert mapper.map_attributes() == expected_result
