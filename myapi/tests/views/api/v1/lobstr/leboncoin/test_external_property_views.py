from rest_framework.test import APIClient
from unittest.mock import patch


class TestExternalPropertyListView:
    def setup_method(self):
        self.client = APIClient()

    @patch(
        "myapi.tasks.lobstr.leboncoin.external_property_create_task."
        "create_external_property_task.delay"
    )
    def test_post_with_id(self, mock_task):
        response = self.client.post(
            "/api/v1/lobstr/leboncoin/external_properties/", data={"id": "12345"}
        )

        mock_task.assert_called_once_with("12345")
        assert response.status_code == 202
        assert response.data == {"status": "Job started"}

    @patch(
        "myapi.tasks.lobstr.leboncoin.external_property_create_task"
        ".create_external_property_task.delay"
    )
    def test_post_without_id(self, mock_task):
        response = self.client.post("/api/v1/lobstr/leboncoin/external_properties/")

        mock_task.assert_not_called()
        assert response.status_code == 400
