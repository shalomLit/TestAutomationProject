import pytest

from infra.config import TestData
from pages.HomePage import HomePage
from pages.LoginUserPage import LogInUser
from tests.test_base import BaseTest


class Test_HomePage(BaseTest):

    @pytest.mark.homePage
    def test_add_project(self):

        self.home_page=HomePage(self.driver)
        self.home_page.do_user_login(TestData.USER_NAME,TestData.PASSWORD)
        self.home_page.do_click_green_plus_button()
        self.home_page.do_click_menu_new_project()





        # self.logInUser=LogInUser(self.driver)
        # self.logInUser.do_user_login(TestData.USER_NAME,TestData.PASSWORD)
        # self.home_page=HomePage(self.driver)
        # self.home_page.plus_button_click()

