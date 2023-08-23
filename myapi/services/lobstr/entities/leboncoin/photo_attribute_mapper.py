class PhotoAttributeMapper:
    def __init__(self, lobstr_property, external_property):
        self.lobstr_property = lobstr_property
        self.external_property = external_property

    def map_attributes(self):
        pictures = self.lobstr_property["pictures"].split("|||")

        return [
            {
                "url": url,
                "position": index + 1,
                "content_object": self.external_property,
            }
            for index, url in enumerate(pictures)
        ]
