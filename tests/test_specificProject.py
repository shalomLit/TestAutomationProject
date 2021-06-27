import pytest

from infra.config import TestData
from pages.HomePage import HomePage
from pages.LoginUserPage import LogInUser
from pages.specific_project import SpecificProject
from tests.test_base import BaseTest


class Test_SpecificProject(BaseTest):

    def test_check_identifier_project(self):

        self.specificProject=SpecificProject(self.driver)
        self.specificProject.do_user_login(TestData.USER_NAME,TestData.PASSWORD)
        self.specificProject.get_to_relevant_url()
        identifier_project=self.specificProject.find_identifire_project()
        expected_identifire_project=self.specificProject.find_expected_identifire_project()
        assert (identifier_project == expected_identifire_project), "the identifier project is different than expected"

    @pytest.mark.specificProject
    def test_check_identifire_in_the_page_corner(self):
        self.specificProject=SpecificProject(self.driver)
        self.specificProject.do_user_login(TestData.USER_NAME,TestData.PASSWORD)
        self.specificProject.get_to_relevant_url()
        corner_page_name_project=self.specificProject.find_identifire_in_the_page_corner()
        assert (corner_page_name_project == TestData.UNIQUE_VALUE_PROJECT_NAME), "the project name in the corner is:{} and we expected to be{}".format(corner_page_name_project,TestData.UNIQUE_VALUE_PROJECT_NAME)








