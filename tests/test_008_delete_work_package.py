import json

import requests
import pytest
from infra.api.config import TestAPI
from infra.api.projects_api import ProjectsApi



@pytest.mark.get_api
def test_delete_work_package():

    projectsApi = ProjectsApi(TestAPI.BASE_URL)

    path = f'/api/v3/projects/{TestAPI.PROJECT_ID_TEST_8}/work_packages/'

    data = {
        "subject": TestAPI.UNIQUE_WORK_PACKAGE_DESCRIPTION_TEST_8
    }

    # create work package
    res = projectsApi.post_project(path,data,201)

    subject=res["subject"]

    # check if it is created properly
    assert subject==TestAPI.UNIQUE_WORK_PACKAGE_DESCRIPTION_TEST_8,\
        f'Expected subject: {TestAPI.UNIQUE_WORK_PACKAGE_DESCRIPTION_TEST_8}'

    # get the all work packages from the project from project id 820
    work_packages_list=projectsApi.get_work_package(path,200)

    # select the id of the last one
    last_work_package_id=work_packages_list["_embedded"]["elements"][len(work_packages_list["_embedded"]["elements"])-1]["id"]

    # from documentation
    path_to_delete=f'/api/v3/work_packages/'

    # delete the last work package
    projectsApi.delete_project(path_to_delete,last_work_package_id,204)

    # Verify the work package was deleted by sending a request to get a work package by ID
    projectsApi.check_project_delete(path,last_work_package_id,404)

















