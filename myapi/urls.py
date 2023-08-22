# myapi/urls.py
from django.urls import include, path
from rest_framework import routers
from myapi.views.api.v1.lobstr.leboncoin.external_property_views import (
    LobstrLeboncoinExternalPropertyViewSet,
)
from myapi.views.api.v1.user.user_external_property_views import (
    UserExternalPropertyViewSet,
)

router = routers.DefaultRouter()
router.register(
    r"user/user_external_properties",
    UserExternalPropertyViewSet,
    basename="user_external_property",
)
router.register(
    r"lobstr/leboncoin/external_properties",
    LobstrLeboncoinExternalPropertyViewSet,
    basename="lobsrt_leboncoin_external_property",
)

urlpatterns = [
    path("api/v1/", include(router.urls)),
]
