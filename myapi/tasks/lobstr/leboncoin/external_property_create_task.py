from celery import shared_task

from myapi.models import ExternalProperty, Photo

from myapi.services.lobstr.lobstr_property_fetcher import LobstrPropertyFetcher
from myapi.services.lobstr.entities.leboncoin_property_attribute_mapper import (
    LeBonCoinPropertyAttributeMapper,
)


@shared_task
def ExternalPropertyCreateTask(run_id):
    property_resuls = LobstrPropertyFetcher(run_id).get_properties()
    if not property_resuls:
        return None

    for leboncoin_property in property_resuls:
        external_property = create_external_properties(leboncoin_property)
        if not external_property:
            return None

        create_photos(leboncoin_property, external_property)


def create_external_properties(leboncoin_property):
    attributes = LeBonCoinPropertyAttributeMapper(leboncoin_property).map_attributes()
    external_property = ExternalProperty(**attributes)
    external_property.clean_and_save()
    return external_property


def create_photos(leboncoin_property, external_property):
    for index, url in enumerate(leboncoin_property["pictures"].split("|||")):
        attributes = {
            "url": url,
            "position": index + 1,
            "external_property_id": external_property.id,
        }

        photo = Photo(**attributes)
        photo.clean_and_save()
