from api_test.endpoints.base_endpoint import BaseEndpoint


class GetMessageEndpoint(BaseEndpoint):
    def __init__(self):
        super().__init__()

    def get_message_request(self, headers, message_id):
        url = f'{BaseEndpoint.base_url}/channels/{BaseEndpoint.channel_id}/messages/{message_id}'
        self.get_request(url, headers)