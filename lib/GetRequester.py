import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        response_data = json.loads(self.get_response_body())
        return response_data


response_data = GetRequester("https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json")
print(response_data.load_json())