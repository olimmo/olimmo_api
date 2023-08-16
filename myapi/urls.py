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

from myapi.views.api.v1.user.user_external_property_views import (
    UserExternalPropertyList,
    SingleUserExternalProperty,
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
                    name="api_v1_seller_property-detail",
                ),
                path(
                    "properties/<int:property_id>",
                    PropertyDetailView.as_view(),
                    name="api_v1_property-detail",
                ),
                path(
                    "seller/<int:seller_id>/properties",
                    SellerPropertyListView.as_view(),
                    name="api_v1_seller_property-detail",
                ),
                path(
                    "seller/<int:seller_id>/properties/<int:property_id>",
                    SellerPropertyDetailView.as_view(),
                    name="api_v1_seller_property-detail",
                ),
                path(
                    "user/user_external_properties/",
                    UserExternalPropertyList.as_view(),
                    name="user_external_properties",
                ),
                path(
                    "user/user_external_properties/<int:user_external_property_id>/",
                    SingleUserExternalProperty.as_view(),
                    name="single_user_external_property",
                ),
                path(
                    "lobstr/leboncoin/external_properties/",
                    LeboncoinExternalPropertyListView.as_view(),
                    name="api_v1_lobstr_leboncoin_external-properties-list",
                ),
            ]
        ),
    ),
]
