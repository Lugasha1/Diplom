from api_test.endpoints.base_endpoint import BaseEndpoint


class PostMessageEndpoint(BaseEndpoint):
    def __init__(self):
        super().__init__()

    def post_message_request(self, headers, data):
        url = f'{BaseEndpoint.base_url}/channels/{BaseEndpoint.channel_id}/messages'
        self.post_request(url, headers, data)

    def get_message_id(self):
        message_id = self.response_json.get('id')
        return message_id