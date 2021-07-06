import json

import requests
import pytest
from infra.api.config import TestAPI
from infra.api.projects_api import ProjectsApi

@pytest.mark.get_api
def test_get_work_package_by_id():

    path='/api/v3/work_packages/'

    projectsApi = ProjectsApi(TestAPI.BASE_URL)


    work_package = projectsApi.get_project(path,TestAPI.WORK_PACKAGE_ID_TEST_5,200)

    type = work_package["_links"]["type"]["title"]

    subject=work_package["subject"]

    assert type == TestAPI.WORK_PACKAGE_TYPE,f'Expected type: {TestAPI.WORK_PACKAGE_TYPE}'

    assert subject == TestAPI.WORK_PACKAGE_SUBJECT,f'Expected type: {TestAPI.WORK_PACKAGE_SUBJECT}'







