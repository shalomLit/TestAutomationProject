import json

import requests
import pytest
from infra.api.config import TestAPI
from infra.api.projects_api import ProjectsApi


# create a new work package with a unique subject.
@pytest.mark.get_api
def test_update_work_package():

    projectsApi = ProjectsApi(TestAPI.BASE_URL)

    path = f'/api/v3/projects/{TestAPI.PROJECT_ID_TEST_7}/work_packages/'

    data = {
        "subject": TestAPI.UNIQUE_WORK_PACKAGE_DESCRIPTION_TEST_7
    }
    # create a subject with post request
    res = projectsApi.post_project(path,data,201)

    # receive the subject name from the response
    subject = res["subject"]

    # check if it the same subject name as the the expected one
    assert subject == TestAPI.UNIQUE_WORK_PACKAGE_DESCRIPTION_TEST_7,\
        f'Expected subject: {TestAPI.UNIQUE_WORK_PACKAGE_DESCRIPTION_TEST_7}'








