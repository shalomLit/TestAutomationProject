import requests
from requests.auth import HTTPBasicAuth

from infra.api.config import TestAPI


class restClient:

    def __init__(self,base_url):
        self.base_url=base_url

    def get(self,path,expected_status_code):
        url=self.base_url+path
        response=requests.get(url,auth=HTTPBasicAuth(TestAPI.USER_NAME, TestAPI.API_KEY))
        assert response.status_code==expected_status_code,f'Expected status code {expected_status_code}'
        return response

    def post(self,path,payload,expected_status_code):
        url=self.base_url+path
        response=requests.post(url,json=payload,auth=HTTPBasicAuth(TestAPI.USER_NAME, TestAPI.API_KEY),
                               headers={"Content-Type": "application/json"})
        assert response.status_code==expected_status_code,f'Expected status code {expected_status_code}'
        return response


    def patch(self,path,payload,expected_status_code):
        url=self.base_url+path
        response=requests.patch(url,json=payload,auth=HTTPBasicAuth(TestAPI.USER_NAME, TestAPI.API_KEY),
                                headers={"Content-Type": "application/json"})
        assert response.status_code==expected_status_code,f'Expected status code {expected_status_code}'
        return response

    def delete(self,path,expected_status_code):
        url=self.base_url+path
        response=requests.delete(url,auth=HTTPBasicAuth(TestAPI.USER_NAME, TestAPI.API_KEY),
                                headers={"Content-Type": "application/json"})
        assert response.status_code==expected_status_code,f'Expected status code {expected_status_code}'
        return response






       # return requests.get(TestAPI.BASE_URL + "/projects/" + TestAPI.PROJECT_ID,
       #                  auth=HTTPBasicAuth('apikey', TestAPI.API_KEY))
