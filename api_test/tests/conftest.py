import pytest

from api_test.endpoints.base_endpoint import BaseEndpoint
from api_test.endpoints.delete_message_endpoint import DeleteMessageEndpoint
from api_test.endpoints.get_message_endpoint import GetMessageEndpoint
from api_test.endpoints.post_message_endpoint import PostMessageEndpoint

API_KEY = BaseEndpoint.api_key


@pytest.fixture()
def headers():
    return {
        'Authorization': f'{API_KEY}',
        'Content-Type': 'application/json'
    }


@pytest.fixture()
def headers_no_token():
    return {
        'Content-Type': 'application/json'
    }

@pytest.fixture()
def get_message_endpoint():
    return GetMessageEndpoint()


@pytest.fixture()
def post_message_endpoint():
    return PostMessageEndpoint()


@pytest.fixture()
def delete_message_endpoint():
    return DeleteMessageEndpoint()