import requests
from requests.auth import HTTPBasicAuth

from infra.api.config import TestAPI


class restClient:

    @staticmethod
    def get_response(self):
       return requests.get(TestAPI.BASE_URL + "/projects/" + TestAPI.PROJECT_ID,
                        auth=HTTPBasicAuth('apikey', TestAPI.API_KEY))
