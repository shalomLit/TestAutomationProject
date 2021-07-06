import requests
import pytest
from requests.auth import HTTPBasicAuth
from infra.api.config import TestAPI
from infra.api.rest_client import restClient

class get_project():

    def test_get_project_by_id(self):

        res=restClient.get_response(self)

        # Validating response code
        status=res.status_code
        assert status==200, "Failed to get correct response code"

        # Parse response to json format
        json_res = res.json()

        # Validating project name
        assert json_res["name"] == TestAPI.PROJECT_TITLE, "Failed to get correct project name"

        # Validating project description
        assert json_res["description"]["raw"] == TestAPI.PROJECT_DESC, "Failed to get correct project description"