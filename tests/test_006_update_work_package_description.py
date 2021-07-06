import json

import requests
import pytest
from infra.api.config import TestAPI
from infra.api.projects_api import ProjectsApi


# update the description of a work package.
@pytest.mark.get_api
def test_update_work_package():

    projectsApi = ProjectsApi(TestAPI.BASE_URL)

    path = '/api/v3/work_packages/'

    # find the lockVersion
    res_work_package=projectsApi.get_project(path,TestAPI.WORK_PACKAGE_ID_TEST_6,200)
    lockVersion = res_work_package["lockVersion"]

    # create body using the lockVersion that we found before
    work_package_data={
        "lockVersion": lockVersion,
        "description": {
            "raw": TestAPI.UNIQUE_WORK_PACKAGE_DESCRIPTION_TEST_6
        }
    }

    res_work_package = projectsApi.update_project(path,TestAPI.WORK_PACKAGE_ID_TEST_5,work_package_data,200)

    # Extract the description
    work_package_description=res_work_package["description"]["raw"]

    #check if the description is the expected one
    assert work_package_description==TestAPI.UNIQUE_WORK_PACKAGE_DESCRIPTION_TEST_6,\
        f'Expected work package description:{TestAPI.UNIQUE_WORK_PACKAGE_DESCRIPTION_TEST_6}'








