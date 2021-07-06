import time

from allure_commons._allure import step
from selenium.webdriver.common.by import By
from allure_commons._allure import step
from selenium.webdriver.common.by import By

from infra.config import TestData
from pages.LoginUserPage import LogInUser

from infra.config import TestData
from pages.basePage import BasePage


class CreateProject(BasePage):

    INPUT_ID_ELEMENT="formly_3_textInput_name_0"
    ADVANCED_SETTING_CLASS="op-fieldset--toggle"
    DESCRIPTION_CLASS_ELEMENT="op-uc-p"

    DESCRIPTION_CLASS_LOCATOR=(By.CLASS_NAME, "op-uc-p")
    #SELECT_STATUS_ELEMENT_XPATH=
    DD_STATUS_XPATH="//*[contains(@id, 'StatusInput__links.status_4')]//input"
    DD_STATUS_OPTION_XPATH="//div[@role='option' and .//span[.='{0}']]"
    SELECT_STATUS_ELEMENT_CLASS="ng-input"
    OPTIONS_CLASS_ELEMENTS="ng-option"
    ON_TRACK_OPTION_TEXT="ON TRACK"
    BUTTON_CLASS_NAME="button"

    def __init__(self,driver):
        super().__init__(driver)

    # ***********************  used to test 9 step 3  ****************************
    @step
    def type_a_unique_value_name(self,unique_value_name):
        input_element=self.get_element_by(By.ID,self.INPUT_ID_ELEMENT)
        self.do_click_by_element(input_element)
        self.do_send_key_to_element(input_element,unique_value_name)
        return True

    # ***********************  used to test 9 step 4  ****************************
    @step
    def click_advanced_setting(self):
        element=self.get_element_by(By.CLASS_NAME,self.ADVANCED_SETTING_CLASS)
        self.do_click_by_element(element)
        return True

    # ***********************  used to test 9 step 5  ****************************
    @step
    def type_to_description_text_box(self):
        element=self.get_element_by(By.CLASS_NAME,self.DESCRIPTION_CLASS_ELEMENT)
        self.do_send_key_to_element(element,TestData.DESCRIPTION_TEXT)
        return True

    # ***********************  used to test 9 step 7  ****************************
    def open_status_dropdown(self):
        element=self.get_element_by_test(By.XPATH,self.DD_STATUS_XPATH)
        self.driver.execute_script("arguments[0].scrollIntoView();",element)
        element.click()

    def select_status_option_dropdown(self):
        element=self.get_element_by(By.XPATH,self.DD_STATUS_OPTION_XPATH.format("On track"))
        element.click()

    @step
    def select_status(self):
        self.open_status_dropdown()
        self.select_status_option_dropdown()
        return True

    # ***********************  used to test 9 step 8  ****************************
    @step
    def click_create(self):
        button=self.get_element_from_list_by_text(By.CLASS_NAME,self.BUTTON_CLASS_NAME,"Save")
        button.click()
        return True

















