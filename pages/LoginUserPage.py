from allure_commons._allure import step
from infra.config import TestData
from pages.basePage import BasePage
from selenium.webdriver.common.by import By


class LogInUser(BasePage):

    # USERNAME_LOCATOR=(By.ID,"username")
    # PASSWORD_LOCATOR=(By.ID,"password")
    #
    # SUBMIT_LOCATOR=(By.NAME,"login")
    #
    # SIGN_IN_LOCAROT_CLASS = "op-app-menu--item-title"
    # SIGN_IN_TEXT = "Sign in"
    # USER_NAME_LOCATOR_ID = "username-pulldown"
    # PASSWORD_LOCATOR_ID = "password-pulldown"
    # LOGIN_PULLDOWN_LOCATOR_ID = "login-pulldown"
    SIGN_IN_LOCAROT_CLASS = "op-app-menu--item-title"
    SIGN_IN_TEXT = "Sign in"
    USER_NAME_LOCATOR_ID = "username-pulldown"
    PASSWORD_LOCATOR_ID = "password-pulldown"
    LOGIN_PULLDOWN_LOCATOR_ID = "login-pulldown"


    # basePage = BasePage(driver)
    #sign_in_element = self.get_element_from_list_by_text(By.CLASS_NAME, SIGN_IN_LOCAROT_CLASS, SIGN_IN_TEXT)
    # basePage.do_click_by_element(sign_in_element)
    #
    # user_name_element = basePage.get_element_by(By.ID, USER_NAME_LOCATOR_ID)
    # password_element = basePage.get_element_by(By.ID, PASSWORD_LOCATOR_ID)
    # login_pulldown_element = basePage.get_element_by(By.ID, LOGIN_PULLDOWN_LOCATOR_ID)
    # basePage.do_send_key_to_element(user_name_element, MY_USER_NAME)
    # basePage.do_send_key_to_element(password_element, MY_PASSWORD)
    # basePage.do_click_by_element(login_pulldown_element)

    def __init__(self, driver):
        super().__init__(driver)
        driver.get(TestData.LOGIN_URL)

    @step
    def do_user_login(self,user_name,password):
        sign_in_element = self.get_element_from_list_by_text(By.CLASS_NAME, self.SIGN_IN_LOCAROT_CLASS, self.SIGN_IN_TEXT)

        self.do_click_by_element(sign_in_element)

        user_name_element = self.get_element_by(By.ID, self.USER_NAME_LOCATOR_ID)
        password_element = self.get_element_by(By.ID, self.PASSWORD_LOCATOR_ID)
        login_pulldown_element = self.get_element_by(By.ID, self.LOGIN_PULLDOWN_LOCATOR_ID)
        self.do_send_key_to_element(user_name_element, user_name)
        self.do_send_key_to_element(password_element, password)
        self.do_click_by_element(login_pulldown_element)
        return True






