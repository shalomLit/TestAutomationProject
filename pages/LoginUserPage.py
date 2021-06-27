from allure_commons._allure import step

from infra.config import TestData
from pages.basePage import BasePage
from selenium.webdriver.common.by import By
class LogInUser(BasePage):

    USERNAME_LOCATOR=(By.ID,"username")
    PASSWORD_LOCATOR=(By.ID,"password")
   # SUBMIT_LOCATOR=(By.XPATH,'//input[@type="submit" and @value="Sign in" and @value="Sign in"]')

    SUBMIT_LOCATOR=(By.NAME,"login")

    SIGN_IN_LOCAROT_CLASS = "op-app-menu--item-title"
    SIGN_IN_TEXT = "Sign in"
    USER_NAME_LOCATOR_ID = "username-pulldown"
    PASSWORD_LOCATOR_ID = "password-pulldown"
    LOGIN_PULLDOWN_LOCATOR_ID = "login-pulldown"
    MY_USER_NAME = "shalom"
    MY_PASSWORD = "1234"

    # basePage = BasePage(driver)
    # sign_in_element = basePage.get_element_from_list_by_text(By.CLASS_NAME, SIGN_IN_LOCAROT_CLASS, SIGN_IN_TEXT)
    # basePage.do_click_by_element(sign_in_element)
    #
    # user_name_element = basePage.get_element_by(By.ID, USER_NAME_LOCATOR_ID)
    # password_element = basePage.get_element_by(By.ID, PASSWORD_LOCATOR_ID)
    # login_pulldown_element = basePage.get_element_by(By.ID, LOGIN_PULLDOWN_LOCATOR_ID)
    # basePage.do_send_key_to_element(user_name_element, MY_USER_NAME)
    # basePage.do_send_key_to_element(password_element, MY_PASSWORD)
    # basePage.do_click_by_element(login_pulldown_element)

    def __init__(self,driver):
        super().__init__(driver,TestData.LOGIN_URL)

    @step
    def do_user_login(self,user_name,password):
        self.do_send_key(self.USERNAME_LOCATOR,user_name)
        self.do_send_key(self.PASSWORD_LOCATOR,password)
        elements=self.get_elements_by(By.NAME,"login")
        self.click_on_element_displayed_from_a_list_of_elements(elements)



