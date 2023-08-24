from celery import shared_task
from myapi.models import ExternalProperty, Photo
from myapi.services.lobstr.lobstr_property_fetcher import LobstrPropertyFetcher
from myapi.services.lobstr.entities.leboncoin.external_property_attribute_mapper import (
    ExternalPropertyAttributeMapper as LeboncoinPropertyMapper,
)
from myapi.services.lobstr.entities.leboncoin.photo_attribute_mapper import (
    PhotoAttributeMapper as LeboncoinPhotoMapper,
)
from myapi.services.lobstr.entities.pap.external_property_attribute_mapper import (
    ExternalPropertyAttributeMapper as PapPropertyMapper,
)
from myapi.services.lobstr.entities.pap.photo_attribute_mapper import (
    PhotoAttributeMapper as PapPhotoMapper,
)

SOURCE_TO_MAPPERS = {
    "leboncoin": {
        "property_mapper": LeboncoinPropertyMapper,
        "photo_mapper": LeboncoinPhotoMapper,
    },
    "pap": {
        "property_mapper": PapPropertyMapper,
        "photo_mapper": PapPhotoMapper,
    },
}


@shared_task
def create_external_property_task(run_id, source):
    lobstr_results = LobstrPropertyFetcher(run_id).get_properties()
    if not lobstr_results:
        return None

    for lobstr_result in lobstr_results:
        attributes = _get_external_property_attributes(lobstr_result, source)
        existing_external_property = _find_existing_external_property(
            attributes, source
        )

        if existing_external_property is not None:
            _update_existing_external_property(existing_external_property, attributes)
        else:
            new_external_property = _create_new_external_property(attributes)
            _create_photos(lobstr_result, new_external_property, source)


# private
def _get_external_property_attributes(lobstr_result, source):
    property_mapper = SOURCE_TO_MAPPERS[source]["property_mapper"]
    return property_mapper(lobstr_result).map_attributes()


def _find_existing_external_property(attributes, source):
    return ExternalProperty.objects.filter(
        source_id=attributes["source_id"], source=source
    ).first()


def _update_existing_external_property(external_property, attributes):
    external_property.price = attributes["price"]
    external_property.clean_and_save()
    return external_property


def _create_new_external_property(attributes):
    external_property = ExternalProperty(**attributes)
    external_property.clean_and_save()
    return external_property


def _get_photo_attributes(external_property, lobstr_result, source):
    photo_mapper = SOURCE_TO_MAPPERS[source]["photo_mapper"]
    return photo_mapper(lobstr_result, external_property).map_attributes()


def _create_photos(lobstr_result, external_property, source):
    if not external_property:
        return None
    photo_attributes = _get_photo_attributes(external_property, lobstr_result, source)
    if not photo_attributes:
        return None

    for attributes in photo_attributes:
        photo = Photo(**attributes)
        photo.clean_and_save()
