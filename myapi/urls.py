# myapi/urls.py
from django.urls import include, path
from rest_framework import routers
from myapi.views.api.v1.property_views import PropertyListView, PropertyDetailView
from myapi.views.api.v1.seller.property_views import (
    PropertyListView as SellerPropertyListView,
    PropertyDetailView as SellerPropertyDetailView,
)
from myapi.views.api.v1.lobstr.leboncoin.external_property_views import (
    ExternalPropertyListView as LeboncoinExternalPropertyListView,
)


router = routers.DefaultRouter()

urlpatterns = [
    path(
        "api/v1/",
        include(
            [
                path(
                    "properties",
                    PropertyListView.as_view(),
                    name="api:v1:seller:property-detail",
                ),
                path(
                    "properties/<int:property_id>",
                    PropertyDetailView.as_view(),
                    name="api:v1:property-detail",
                ),
                path(
                    "seller/<int:seller_id>/properties",
                    SellerPropertyListView.as_view(),
                    name="api:v1:seller:property-detail",
                ),
                path(
                    "seller/<int:seller_id>/properties/<int:property_id>",
                    SellerPropertyDetailView.as_view(),
                    name="api:v1:seller:property-detail",
                ),
                path(
                    "lobstr/leboncoin/external_properties",
                    LeboncoinExternalPropertyListView.as_view(),
                    name="api:v1:lobstr:leboncoin:external-properties-list",
                ),
            ]
        ),
    )
]
