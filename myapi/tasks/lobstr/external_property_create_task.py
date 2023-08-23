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
    "Leboncoin": {
        "property_mapper": LeboncoinPropertyMapper,
        "photo_mapper": LeboncoinPhotoMapper,
    },
    "PAP": {
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
        external_property = _create_external_properties(lobstr_result, source)
        if external_property:
            _create_photos(lobstr_result, external_property, source)


# private
def _create_external_properties(lobstr_result, source):
    mapper_class = SOURCE_TO_MAPPERS[source]["property_mapper"]
    attributes = mapper_class(lobstr_result).map_attributes()
    external_property = ExternalProperty(**attributes)
    external_property.clean_and_save()
    return external_property


def _create_photos(lobstr_result, external_property, source):
    mapper_class = SOURCE_TO_MAPPERS[source]["photo_mapper"]
    photo_attributes = mapper_class(lobstr_result, external_property).map_attributes()

    if not photo_attributes:
        return None

    for attributes in photo_attributes:
        photo = Photo(**attributes)
        photo.clean_and_save()
