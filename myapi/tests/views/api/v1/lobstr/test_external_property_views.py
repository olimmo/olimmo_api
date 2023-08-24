from rest_framework.test import APIClient
from unittest.mock import patch


class TestLobstrExternalPropertyViewSet:
    def setup_method(self):
        self.client = APIClient()

    @patch(
        "myapi.tasks.lobstr.external_property_create_task.create_external_property_task.delay"
    )
    def test_create_with_id_and_cluster(self, mock_task):
        response = self.client.post(
            "/api/v1/lobstr/external_properties/",
            data={"id": "12345", "cluster": "pap"},
        )

        mock_task.assert_called_once_with("12345", "pap")
        assert response.status_code == 202
        assert response.data == {"status": "Job started"}

    @patch(
        "myapi.tasks.lobstr.external_property_create_task.create_external_property_task.delay"
    )
    def test_create_without_id(self, mock_task):
        response = self.client.post(
            "/api/v1/lobstr/external_properties/", data={"cluster": "pap"}
        )

        mock_task.assert_not_called()
        assert response.status_code == 400

    @patch(
        "myapi.tasks.lobstr.external_property_create_task.create_external_property_task.delay"
    )
    def test_create_without_cluster(self, mock_task):
        response = self.client.post(
            "/api/v1/lobstr/external_properties/", data={"id": "12345"}
        )

        mock_task.assert_not_called()
        assert response.status_code == 400
