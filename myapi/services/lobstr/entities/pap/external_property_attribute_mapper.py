import re


class ExternalPropertyAttributeMapper:
    def __init__(self, lobstr_property):
        self.lobstr_property = lobstr_property

    def map_attributes(self):
        return {
            "currency": self._get_currency(),
            "city": self._extract_city_and_postal_code("city"),
            "description": self._get_property("description"),
            "energy_rate": self._get_property("energy"),
            "first_photo_url": self._get_first_photo_url(),
            "gps_latitude": self._get_property("lat"),
            "gps_longitude": self._get_property("lng"),
            "greenhouse_gas": self._get_property("ges"),
            "nb_bedrooms": self._get_property("bedrooms"),
            "nb_rooms": self._get_property("rooms"),
            "postal_code": self._extract_city_and_postal_code("postal_code"),
            "price": self._get_property("price"),
            "seller_phone": self._get_seller_phone(),
            "source": "pap",
            "source_id": self._get_property("internal_id"),
            "surface": self._get_property("size"),
            "title": self._get_property("title"),
            "url": self._get_property("url"),
        }

    def _get_currency(self):
        return "USD" if self._get_property("currency") == "dollar" else "EUR"

    def _get_first_photo_url(self):
        image_urls = self._get_property("image_urls")
        return image_urls.split(",")[0].strip() if image_urls else None

    def _get_seller_phone(self):
        phone = self._get_property("phone")
        return phone.replace(".", "") if phone else None

    def _extract_city_and_postal_code(self, requested_part):
        neighborhood = self._get_property("neighborhood")
        match = re.match(r"^(.*?)\s*\((.*?)\)$", neighborhood)
        if not match:
            return None

        if requested_part == "city":
            return match.group(1).strip()
        elif requested_part == "postal_code":
            return match.group(2).strip()

    def _get_property(self, key):
        if self.lobstr_property[key]:
            return self.lobstr_property[key]
        else:
            return None
