import time

import pytest

from infra.config import TestData
from pages.HomePage import HomePage
from pages.LoginUserPage import LogInUser
from pages.createProjectPage import CreateProject
from tests.test_base import BaseTest


class Test_CreateProjec(BaseTest):

    @pytest.mark.createProject
    def test_type_a_unique_value_name(self):

        self.createProject=CreateProject(self.driver)
        self.createProject.do_user_login(TestData.USER_NAME,TestData.PASSWORD)
        self.createProject.get_to_relevant_url()
        self.createProject.type_a_unique_value_name(TestData.UNIQUE_VALUE_PROJECT_NAME)
        self.createProject.click_advanced_setting()
        self.createProject.type_to_description_text_box()
        self.createProject.select_status()
        self.createProject.click_create()
        time.sleep(6)





        # self.logInUser=LogInUser(self.driver)
        # self.logInUser.do_user_login(TestData.USER_NAME,TestData.PASSWORD)
        # self.home_page=HomePage(self.driver)
        # self.home_page.plus_button_click()



