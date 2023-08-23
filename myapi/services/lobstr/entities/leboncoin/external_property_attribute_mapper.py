class ExternalPropertyAttributeMapper:
    def __init__(self, lobstr_property):
        self.lobstr_property = lobstr_property
        self.more_details = lobstr_property.get("more_details", {})

    def map_attributes(self):
        return {
            "currency": self.lobstr_property["currency"],
            "city": self.lobstr_property["department"],
            "description": self.lobstr_property["description"],
            "elevator": self.more_details.get("elevator") == "Oui",
            "energy_rate": self._filter_invalid_values(
                self.lobstr_property["DPE_string"]
            ),
            "first_photo_url": self.lobstr_property["pictures"].split("|||")[0],
            "floor_number": self._to_integer(self.more_details.get("floor_number")),
            "gps_latitude": self.lobstr_property["lat"],
            "gps_longitude": self.lobstr_property["lng"],
            "greenhouse_gas": self._filter_invalid_values(
                self.lobstr_property["GES_string"]
            ),
            "nb_bedrooms": self._to_integer(
                self.more_details.get("sleepingroom_count")
            ),
            "nb_floors_building": self._to_integer(
                self.more_details.get("nb_floors_building")
            ),
            "nb_parkings": self._to_integer(self.more_details.get("nb_parkings")),
            "nb_rooms": self._to_integer(self.more_details.get("rooms")),
            "outside_access": self.more_details.get("outside_access"),
            "postal_code": self.lobstr_property["postal_code"],
            "price": self.lobstr_property["price"],
            "property_type": self.more_details.get("real_estate_type"),
            "region": self.lobstr_property["region"],
            "seller_email": self.lobstr_property["mail"],
            "seller_name": self.lobstr_property["owner_name"],
            "seller_phone": self.lobstr_property["phone"],
            "source": "Leboncoin",
            "source_id": self.lobstr_property["annonce_id"],
            "surface": self.lobstr_property["area"],
            "title": self.lobstr_property["title"],
            "url": self.lobstr_property["url"],
        }

    @staticmethod
    def _filter_invalid_values(value):
        return value if value not in ["Vierge", "Non renseigné"] else None

    @staticmethod
    def _to_integer(value):
        try:
            return int(value)
        except TypeError:
            return None
