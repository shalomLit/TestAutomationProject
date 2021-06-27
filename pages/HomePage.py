import time

from allure_commons._allure import step
from basepage import BasePage
from selenium.webdriver.common.by import By

from infra.config import TestData
from pages.LoginUserPage import LogInUser


class HomePage(BasePage,LogInUser):


    PLUS_BUTTON_XPATH = '//*[@id="wrapper"]/header/div[1]/ul/li[2]/a/i'
    NEW_PROJECT_XPATH='//a[@aria-label="New project"]'


    def __init__(self,driver):
        super().__init__(driver)
        driver.get(TestData.USER_LOGIN_URL)


    def wait(self):
        time.sleep(5)

    @step
    def do_click_green_plus_button(self):
        element=self.get_element_by(By.XPATH,self.PLUS_BUTTON_XPATH)
        self.do_click_by_element(element)

    @step
    def do_click_menu_new_project(self):
        element=self.get_element_by(By.XPATH,self.NEW_PROJECT_XPATH)
        print(element)
        self.do_click_by_element(element)













