from rest_framework.test import APIClient
from myapi.tests.factories import CustomUserFactory
from myapi.views.api.v1.user.mixins import UserAuthenticationMixin
from rest_framework.views import APIView
from rest_framework.response import Response


# This is a simple view that uses your mixin just for testing purposes.
class DummyView(UserAuthenticationMixin, APIView):
    def get(self, request, *args, **kwargs):
        return Response({"status": "ok"})


class TestUserAuthenticationMixin:
    def setup_method(self):
        self.client = APIClient()

    def test_valid_uid_header(self):
        user = CustomUserFactory()
        self.client.credentials(HTTP_UID=user.email)
        response = self.client.get("/api/v1/user/user_external_properties/")

        assert response.status_code == 200
        assert response.data == []

    def test_missing_uid_header(self):
        response = self.client.get("/api/v1/user/user_external_properties/")

        assert response.status_code == 400
        assert response.data == {"detail": "Missing HTTP_UID header"}

    def test_invalid_uid_header(self):
        self.client.credentials(HTTP_UID="nonexistentemail@example.com")
        response = self.client.get("/api/v1/user/user_external_properties/")

        assert response.status_code == 404
        assert response.data == {"detail": "User not found"}
