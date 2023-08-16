from rest_framework.test import APITestCase
from myapi.tests.factories import CustomUserFactory, UserExternalPropertyFactory


class UserExternalPropertyListTests(APITestCase):
    def test_when_user_has_external_properties(self):
        # Setup
        property_1 = UserExternalPropertyFactory()
        UserExternalPropertyFactory()
        self.client.credentials(HTTP_UID=property_1.user.email)

        # Make the request
        response = self.client.get("/api/v1/user/user_external_properties/")

        # Assertions
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

    def test_when_user_has_no_external_property(self):
        # Setup
        user = CustomUserFactory()
        self.client.credentials(HTTP_UID=user.email)

        # Make the request
        response = self.client.get("/api/v1/user/user_external_properties/")

        # Assertions
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 0)

    def test_when_missing_uid_header(self):
        # Setup
        self.client.credentials()

        response = self.client.get("/api/v1/user/user_external_properties/")
        # Make the request

        # Assertions
        self.assertEqual(response.status_code, 400)
        self.assertIn("detail", response.data)
        self.assertEqual(response.data["detail"], "Missing HTTP_UID header")


class SingleUserExternalPropertyTests(APITestCase):
    def test_retreive_when_user_has_user_external_property(self):
        # Setup
        user_external_property = UserExternalPropertyFactory()
        self.client.credentials(HTTP_UID=user_external_property.user.email)

        # Make the request
        url = f"/api/v1/user/user_external_properties/{user_external_property.id}/"
        response = self.client.get(url)

        # Assertions
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["id"], user_external_property.id)

    def test_retreive_when_user_has_no_user_external_property(self):
        # Setup
        user = CustomUserFactory()
        self.client.credentials(HTTP_UID=user)

        # Make the request
        url = "/api/v1/user/user_external_properties/1/"
        response = self.client.get(url)

        # Assertions
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.data["detail"], "User not found")

    def test_retreive_when_missing_uid_header(self):
        # Setup
        user_external_property = UserExternalPropertyFactory()

        # Make the request
        url = f"/api/v1/user/user_external_properties/{user_external_property.id}/"
        response = self.client.get(url)

        # Assertions
        self.assertEqual(response.status_code, 400)
        self.assertIn("detail", response.data)
        self.assertEqual(response.data["detail"], "Missing HTTP_UID header")

    def test_update_with_valid_params(self):
        # Setup
        user_external_property = UserExternalPropertyFactory(state="waiting")
        self.client.credentials(HTTP_UID=user_external_property.user.email)

        # Make the request
        params = {"state": "contacted"}
        url = f"/api/v1/user/user_external_properties/{user_external_property.id}/"
        response = self.client.put(url, params)
        user_external_property.refresh_from_db()

        # Assertions
        assert response.status_code == 200
        assert user_external_property.state == "contacted"

    def test_update_with_invalid_params(self):
        # Setup
        user_external_property = UserExternalPropertyFactory(state="waiting")
        self.client.credentials(HTTP_UID=user_external_property.user.email)

        # Make the request
        params = {"state": "wrong_state"}
        url = f"/api/v1/user/user_external_properties/{user_external_property.id}/"
        response = self.client.put(url, params)
        user_external_property.refresh_from_db()

        # Assertions
        assert response.status_code == 400
        assert user_external_property.state == "waiting"

    def test_update_when_missing_uid_header(self):
        # Setup
        user_external_property = UserExternalPropertyFactory()

        # Make the request
        url = f"/api/v1/user/user_external_properties/{user_external_property.id}/"
        params = {"state": "contacted"}
        response = self.client.put(url, params)

        # Assertions
        self.assertEqual(response.status_code, 400)
        self.assertIn("detail", response.data)
        self.assertEqual(response.data["detail"], "Missing HTTP_UID header")
