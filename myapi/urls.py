# myapi/urls.py
from django.urls import path
from rest_framework import routers
from myapi.views.api.v1 import PropertyListView, PropertyDetailView
from myapi.views.api.v1.seller import (
    PropertyListView as SellerPropertyListView,
    PropertyDetailView as SellerPropertyDetailView,
)


router = routers.DefaultRouter()

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("api/v1/properties", PropertyListView.as_view(), name="property-list"),
    path(
        "api/v1/properties/<int:pk>",
        PropertyDetailView.as_view(),
        name="property-detail",
    ),
    path(
        "api/v1/seller/<int:seller_id>/properties",
        SellerPropertyListView.as_view(),
        name="seller-properties-list",
    ),
    path(
        "api/v1/seller/<int:seller_id>/properties/<int:property_id>",
        SellerPropertyDetailView.as_view(),
        name="seller-property-detail",
    ),
]
