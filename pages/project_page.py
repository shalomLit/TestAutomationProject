import time

from allure_commons._allure import step
from selenium.webdriver.common.by import By

from infra.ui.config import TestData
from pages.basePage import BasePage

class ProjectPage (BasePage):

    LEFT_CORNER_CLASS_NAME = "op-app-menu--item-title"

    def __init__(self,driver):
        super().__init__(driver)

    # ***********************  used to test 9 step 9  ****************************
    @step
    def find_identifire_in_the_page_corner(self):
        time.sleep(1)
        corner_element=self.get_element_from_list_by_text(By.CLASS_NAME,self.LEFT_CORNER_CLASS_NAME,TestData.UNIQUE_VALUE_PROJECT_NAME)
        if corner_element is None:
            return False
        return corner_element.text




    # @step
    # def find_identifire_project(self):
    #     current_url = self.driver.current_url
    #     url_list_divided_by_slash = current_url.split("/")
    #     identifire_project = url_list_divided_by_slash[len(url_list_divided_by_slash) - 2]
    #     return identifire_project
    #
    # @step
    # def find_expected_identifire_project(self):
    #     origin_project_name=TestData.UNIQUE_VALUE_PROJECT_NAME
    #     expected_project_name=""
    #     special_characters=["!","@","#","$","%","^","&","*","(",")","_","+"," "]
    #     for i in origin_project_name:
    #         if i.isupper():
    #             expected_project_name=expected_project_name+ i.lower()
    #         elif i in special_characters:
    #             expected_project_name=expected_project_name+"-"
    #         else:
    #             expected_project_name=expected_project_name+i
    #     return expected_project_name














