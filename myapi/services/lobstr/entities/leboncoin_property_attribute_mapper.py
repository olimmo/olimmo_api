class LeBonCoinPropertyAttributeMapper:
    def __init__(self, leboncoin_property):
        self.leboncoin_property = leboncoin_property
        self.more_details = leboncoin_property.get("more_details", {})

    def map_attributes(self):
        return {
            "currency": self.leboncoin_property["currency"],
            "city": self.leboncoin_property["department"],
            "description": self.leboncoin_property["description"],
            "elevator": self.more_details.get("elevator") == "Oui",
            "energy_rate": self.leboncoin_property["DPE_string"],
            "first_photo_url": self.more_details.get("profile_picture_url"),
            "floor_number": self._to_integer(self.more_details.get("floor_number")),
            "gps_latitude": self.leboncoin_property["lat"],
            "gps_longitude": self.leboncoin_property["lng"],
            "greenhouse_gas": self._greenhouse_gas(self.leboncoin_property),
            "nb_bedrooms": self._to_integer(
                self.more_details.get("sleepingroom_count")
            ),
            "nb_floors_building": self._to_integer(
                self.more_details.get("nb_floors_building")
            ),
            "nb_parkings": self._to_integer(self.more_details.get("nb_parkings")),
            "nb_rooms": self._to_integer(self.more_details.get("rooms")),
            "outside_access": self.more_details.get("outside_access"),
            "postal_code": self.leboncoin_property["postal_code"],
            "price": self.leboncoin_property["price"],
            "property_type": self.more_details.get("real_estate_type"),
            "region": self.leboncoin_property["region"],
            "seller_email": self.leboncoin_property["mail"],
            "seller_name": self.leboncoin_property["owner_name"],
            "seller_phone": self.leboncoin_property["phone"],
            "source": "Leboncoin",
            "source_id": self.leboncoin_property["annonce_id"],
            "surface": self.leboncoin_property["area"],
            "title": self.leboncoin_property["title"],
            "url": self.leboncoin_property["url"],
        }

    @staticmethod
    def _greenhouse_gas(leboncoin_property):
        ges_string = leboncoin_property["GES_string"]
        return ges_string if ges_string != "Vierge" else None

    @staticmethod
    def _to_integer(value):
        try:
            return int(value)
        except TypeError:
            return None
