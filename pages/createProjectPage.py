import time

from allure_commons._allure import step
from basepage import BasePage
from selenium.webdriver.common.by import By

from infra.config import TestData
from pages.LoginUserPage import LogInUser


class CreateProject(BasePage,LogInUser):

    INPUT_ID_ELEMENT="formly_3_textInput_name_0"
    ADVANCED_SETTING_CLASS="op-fieldset--toggle"
    DESCRIPTION_CLASS_ELEMENT="op-uc-p"
    SELECT_STATUS_ELEMENT_XPATH= '//*[@id="formly_9_selectProjectStatusInput__links.status_4"]/div/div/div[3]/input'
    SELECT_STATUS_ELEMENT_CLASS="ng-input"
    OPTIONS_CLASS_ELEMENTS="ng-option"
    ON_TRACK_OPTION_TEXT="ON TRACK"
    BUTTON_CLASS_NAME="button"





    def __init__(self,driver):
        super().__init__(driver)
        driver.get(TestData.USER_LOGIN_URL)

    @step
    def get_to_relevant_url(self):

       self.driver.get(TestData.PROJECT_PAGE_URL)


    @step
    def type_a_unique_value_name(self,unique_value_name):
        input_element=self.get_element_by(By.ID,self.INPUT_ID_ELEMENT)
        self.do_click_by_element(input_element)
        self.do_send_key_to_element(input_element,unique_value_name)

    @step
    def click_advanced_setting(self):
        element=self.get_element_by(By.CLASS_NAME,self.ADVANCED_SETTING_CLASS)
        self.do_click_by_element(element)

    @step
    def type_to_description_text_box(self):
        description_element=self.get_element_by(By.CLASS_NAME,self.DESCRIPTION_CLASS_ELEMENT)
        self.do_click_by_element(description_element)
        self.do_send_key_to_element(description_element,TestData.DESCRIPTION_TEXT)


    @step
    def select_status(self):
        select_element=self.get_element_by(By.XPATH,self.SELECT_STATUS_ELEMENT_XPATH)
        self.do_click_by_element(select_element)
        on_track_option=self.get_element_from_list_by_text(By.CLASS_NAME,self.OPTIONS_CLASS_ELEMENTS,self.ON_TRACK_OPTION_TEXT)
        self.do_click_by_element(on_track_option)

    @step
    def click_create(self):
        button=self.get_element_from_list_by_text(By.CLASS_NAME,self.BUTTON_CLASS_NAME,"Save")
        self.do_click_by_element(button)
















