class PhotoAttributeMapper:
    def __init__(self, lobstr_property, external_property):
        self.lobstr_property = lobstr_property
        self.external_property = external_property

    def map_attributes(self):
        image_urls = self._get_image_urls()
        if image_urls:
            return [
                self._build_attribute(url, index)
                for index, url in enumerate(image_urls)
            ]

    def _get_image_urls(self):
        image_urls_str = self.lobstr_property.get("image_urls")
        if image_urls_str is None or not image_urls_str.strip():
            return None

        return image_urls_str.replace(" ", "").split(",")

    def _build_attribute(self, url, index):
        if url.startswith("https://"):
            return {
                "url": url,
                "position": index + 1,
                "content_object": self.external_property,
            }
