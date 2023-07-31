import pytest
import requests_mock

from myapi.services.lobstr.lobstr_property_fetcher import LobstrPropertyFetcher


@pytest.fixture
def mock_request():
    with requests_mock.Mocker() as m:
        yield m


@pytest.fixture
def url():
    return "https://api.lobstr.io/v1/results?run=run_id"


class TestLobstrPropertyFetcher:
    def test_get_properties_no_run_id(self):
        service = LobstrPropertyFetcher(None)

        result = service.get_properties()
        assert result is None

    def test_get_properties_error_status(self, mock_request, url):
        mock_request.get(url, status_code=400)
        fetcher = LobstrPropertyFetcher("run_id")
        result = fetcher.get_properties()
        assert result is None

    def test_get_properties_success(self, mock_request, url):
        mock_request.get(url, status_code=200, json={"data": "test_data"})
        fetcher = LobstrPropertyFetcher("run_id")
        result = fetcher.get_properties()
        assert result == "test_data"
