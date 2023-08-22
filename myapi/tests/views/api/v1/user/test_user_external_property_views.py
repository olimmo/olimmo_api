import pytest
from rest_framework.test import APIClient
from rest_framework import status
from myapi.tests.factories import (
    CustomUserFactory,
    ExternalPropertyFactory,
)
from myapi.models import UserExternalProperty


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def user():
    return CustomUserFactory()


@pytest.fixture
def external_properties(user):
    return [ExternalPropertyFactory(), ExternalPropertyFactory()]


@pytest.mark.django_db
class TestUserExternalPropertyViewSet:
    base_url = "/api/v1/user/user_external_properties/"

    def test_list_user_external_properties(self, api_client, user, external_properties):
        UserExternalProperty.objects.all().update(user=user)
        api_client.credentials(HTTP_UID=user.email)
        response = api_client.get(self.base_url)

        assert response.status_code == status.HTTP_200_OK
        assert len(response.json()) == 2

    def test_list_filtered_by_state(self, api_client, user, external_properties):
        property = UserExternalProperty.objects.first()
        property.state = "contacted"
        property.save()
        UserExternalProperty.objects.all().update(user=user)
        api_client.credentials(HTTP_UID=user.email)
        response = api_client.get(self.base_url, {"state": "contacted"})

        assert response.status_code == status.HTTP_200_OK
        assert len(response.json()) == 1
        assert response.json()[0]["state"] == "contacted"

    def test_list_ordered_by_created_at_asc(
        self, api_client, user, external_properties
    ):
        UserExternalProperty.objects.all().update(user=user)
        api_client.credentials(HTTP_UID=user.email)
        response = api_client.get(self.base_url, {"order_by": "created_at"})

        assert response.status_code == status.HTTP_200_OK
        assert len(response.json()) == 2
        assert response.json()[0]["created_at"] < response.json()[1]["created_at"]

    def test_list_ordered_by_created_at_desc(
        self, api_client, user, external_properties
    ):
        UserExternalProperty.objects.all().update(user=user)
        api_client.credentials(HTTP_UID=user.email)
        response = api_client.get(self.base_url, {"order_by": "-created_at"})

        assert response.status_code == status.HTTP_200_OK
        assert len(response.json()) == 2
        assert response.json()[0]["created_at"] > response.json()[1]["created_at"]

    def test_list_ordered_by_a_wrong_attribute(
        self, api_client, user, external_properties
    ):
        UserExternalProperty.objects.all().update(user=user)
        api_client.credentials(HTTP_UID=user.email)
        response = api_client.get(self.base_url, {"order_by": "-id"})

        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_list_with_included_relationships(
        self, api_client, user, external_properties
    ):
        UserExternalProperty.objects.all().update(user=user)
        api_client.credentials(HTTP_UID=user.email)
        response = api_client.get(self.base_url, {"included": "external_property"})

        assert response.status_code == status.HTTP_200_OK
        assert len(response.json()) == 2
        assert response.json()[0]["external_property"] is not None

    def test_list_with_wrong_included_relationships(
        self, api_client, user, external_properties
    ):
        UserExternalProperty.objects.all().update(user=user)
        api_client.credentials(HTTP_UID=user.email)
        response = api_client.get(self.base_url, {"included": "wrong_relation"})

        assert response.status_code == status.HTTP_200_OK
        assert len(response.json()) == 2
        assert response.json()[0] is not None
        assert "wrong_attribute" not in response.json()[0]

    def test_list_with_nested_relationships(
        self, api_client, user, external_properties
    ):
        UserExternalProperty.objects.all().update(user=user)
        api_client.credentials(HTTP_UID=user.email)
        response = api_client.get(
            self.base_url, {"included": "external_property,photos"}
        )

        assert response.status_code == status.HTTP_200_OK
        assert len(response.json()) == 2
        assert response.json()[0]["external_property"]["photos"] is not None

    def test_list_with_wrong_nested_relationships(
        self, api_client, user, external_properties
    ):
        UserExternalProperty.objects.all().update(user=user)
        api_client.credentials(HTTP_UID=user.email)
        response = api_client.get(
            self.base_url, {"included": "external_property,wrong_relation"}
        )

        assert response.status_code == status.HTTP_200_OK
        assert len(response.json()) == 2
        assert response.json()[0]["external_property"] is not None
        assert "wrong_attribute" not in response.json()[0]["external_property"]

    def test_missing_uid_header(self, api_client):
        response = api_client.get(self.base_url)
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_user_with_no_user_external_properties(self, api_client, user):
        # Ensure the user has no user_external_properties
        UserExternalProperty.objects.filter(user=user).delete()

        api_client.credentials(HTTP_UID=user.email)
        response = api_client.get(self.base_url)

        assert response.status_code == status.HTTP_200_OK
        assert len(response.json()) == 0

    def test_retrieve_user_external_property(
        self, api_client, user, external_properties
    ):
        UserExternalProperty.objects.all().update(user=user)
        property_instance = external_properties[0].userexternalproperty_set.first()
        api_client.credentials(HTTP_UID=user.email)
        url = f"{self.base_url}{property_instance.id}/"
        response = api_client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert response.json()["id"] == property_instance.id

    def test_update_user_external_property(self, api_client, user, external_properties):
        UserExternalProperty.objects.all().update(user=user)
        property_instance = external_properties[0].userexternalproperty_set.first()
        api_client.credentials(HTTP_UID=user.email)
        url = f"{self.base_url}{property_instance.id}/"
        data = {"state": "contacted"}
        response = api_client.put(url, data, format="json")

        property_instance.refresh_from_db()
        assert response.status_code == status.HTTP_200_OK
        assert property_instance.state == "contacted"

    def test_update_with_invalid_data(self, api_client, user, external_properties):
        UserExternalProperty.objects.all().update(user=user)
        property_instance = external_properties[0].userexternalproperty_set.first()
        api_client.credentials(HTTP_UID=user.email)
        url = f"{self.base_url}{property_instance.id}/"
        data = {"state": "invalid_state"}
        response = api_client.put(url, data, format="json")

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert "state" in response.json().keys()
