import json

import requests
import pytest
from requests.auth import HTTPBasicAuth
from infra.api.config import TestAPI
from infra.api.projects_api import ProjectsApi
from infra.api.rest_client import restClient


@pytest.mark.get_api
def test_update_project_by_id():

    projectsApi=ProjectsApi(TestAPI.BASE_URL)

    path = '/api/v3/projects/'

    project_data={"description": {
        "raw": TestAPI.UNIQUE_DESCRIPTION_PROJECT_TEST_2
    }}

    project = projectsApi.update_project(path,TestAPI.PROJECT_ID_TEST_2,project_data,200)

    assert project["description"]["raw"] == TestAPI.UNIQUE_DESCRIPTION_PROJECT_TEST_2,\
        f'Expected project description: {TestAPI.UNIQUE_DESCRIPTION_PROJECT_TEST_2}'






