# myapi/urls.py
from django.urls import include, path
from rest_framework import routers
from myapi.views.api.v1 import PropertyList, PropertyDetail


router = routers.DefaultRouter()

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/v1/properties/', PropertyList.as_view()),
    path('api/v1/properties/<int:pk>/', PropertyDetail.as_view()),
]
