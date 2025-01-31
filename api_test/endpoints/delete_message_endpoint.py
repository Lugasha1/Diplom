import requests

from api_test.endpoints.base_endpoint import BaseEndpoint


class DeleteMessageEndpoint(BaseEndpoint):
    def __init__(self):
        super().__init__()

    def delete_message(self, headers, message_id):
        url = f'{BaseEndpoint.base_url}/channels/{BaseEndpoint.channel_id}/messages/{message_id}'
        self.response = requests.delete(url=url, headers=headers, verify=False)
        return self.response.status_code