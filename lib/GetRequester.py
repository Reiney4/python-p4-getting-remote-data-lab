import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url) 
        return response.content

    def load_json(self):
        responses = json.loads(self.get_response_body())
        return responses  
    
URL = 'https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json'
CONVERTED_DATA = [
    {'name': 'Daniel', 'occupation': 'LG Fridge Salesman'},
    {'name': 'Joe', 'occupation': 'WiFi Fixer'},
    {'name': 'Avi', 'occupation': 'DJ'},
    {'name': 'Howard', 'occupation': 'Mountain Legend'}
]

def test_get_response():
    '''get_response_body function returns response.'''
    requester = GetRequester(URL)
    assert requester.get_response_body() == JSON_STRING

def test_load_json():
    '''load_json function returns response.'''
    requester = GetRequester(URL)
    assert requester.load_json() == CONVERTED_DATA

if __name__ == '__main__':
    test_get_response()
    test_load_json()
