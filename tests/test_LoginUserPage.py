import pytest

from infra.config import TestData
from pages.LoginUserPage import LogInUser
from tests.test_base import BaseTest


class Test_LoginUserPage(BaseTest):
    @pytest.mark.userLogin
    def test_login_user(self):
        self.logInUser=LogInUser(self.driver)
        self.logInUser.do_user_login(TestData.USER_NAME,TestData.PASSWORD)