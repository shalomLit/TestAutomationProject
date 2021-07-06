import requests
import pytest
from requests.auth import HTTPBasicAuth
from infra.api.config import TestAPI
from infra.api.projects_api import ProjectsApi
from infra.api.rest_client import restClient


@pytest.mark.get_api11111111
def test_get_project_by_id():

    path='/api/v3/projects/'

    projectsApi = ProjectsApi(TestAPI.BASE_URL)
    project=projectsApi.get_project(path,TestAPI.PROJECT_ID_TEST_1,200)

    project_name=project["name"]
    assert project_name==TestAPI.EXPECTED_PROJECT_NAME,\
        f'Expected project name: {TestAPI.EXPECTED_PROJECT_NAME}'

    project_description =project["description"]["raw"]

    assert project_description == TestAPI.EXPECTED_PROJECT_DESCRIPTION,\
        f'Expected project name: {TestAPI.EXPECTED_PROJECT_DESCRIPTION }'


