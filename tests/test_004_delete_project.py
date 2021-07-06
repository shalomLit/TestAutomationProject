import json
import time

import requests
import pytest
from infra.api.config import TestAPI
from infra.api.projects_api import ProjectsApi

@pytest.mark.get_api
def test_delete_project_by_id():

    path='/api/v3/projects/'

    projectsApi = ProjectsApi(TestAPI.BASE_URL)

    project_data = {
        "name": TestAPI.UNIQUE_PROJECT_NAME_TO_DELETE_STEP_4
    }

    # create project
    project=projectsApi.post_project(path,project_data,201)

    # check the project name
    assert project["name"] == TestAPI.UNIQUE_PROJECT_NAME_TO_DELETE_STEP_4,\
        f'Expected project description: {TestAPI.UNIQUE_PROJECT_NAME_TO_DELETE_STEP_4}'

    project_id=project["id"]

    # delete the project by sending the project id how created just now
    projectsApi.delete_project(path,project_id,204)

    # sending get request with expected code-404
    time.sleep(3)
    projectsApi.check_project_delete(path,project_id,404)





