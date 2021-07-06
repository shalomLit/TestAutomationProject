import json

import requests
import pytest
from infra.api.config import TestAPI
from infra.api.projects_api import ProjectsApi


# create project with a unique name
@pytest.mark.get_api
def test_create_project():

    projectsApi = ProjectsApi(TestAPI.BASE_URL)

    path='/api/v3/projects'

    project_data = {
        "name": TestAPI.UNIQUE_PROJECT_NAME_FOR_STEP_3
    }

    project=projectsApi.post_project(path,project_data,201)

    project_name=project["name"]

    assert project_name==TestAPI.UNIQUE_PROJECT_NAME_FOR_STEP_3,\
        f'Expected project description: {TestAPI.UNIQUE_PROJECT_NAME_FOR_STEP_3}'

