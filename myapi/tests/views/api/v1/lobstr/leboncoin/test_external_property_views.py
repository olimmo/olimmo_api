import pytest
from unittest.mock import patch


# Fixtures
@pytest.fixture
def url():
    return "/api/v1/lobstr/leboncoin/external_properties"


@pytest.fixture()
def mocked_task():
    with patch(
        "myapi.views.api.v1.lobstr.leboncoin.external_property_views"
        ".create_external_property_task.delay"
    ) as mock_delay:
        yield mock_delay


# Test cases
def test_external_property_create_view_no_run_id(mocked_task, client, url):
    response = client.post(url, data={"id": ""})

    assert response.status_code == 400
    assert not response.data
    assert not mocked_task.called


def test_external_property_create_view(mocked_task, client, url):
    response = client.post(url, data={"id": "1234567890"})

    assert response.status_code == 202
    assert response.data == {"status": "Job started"}
    assert mocked_task.called
