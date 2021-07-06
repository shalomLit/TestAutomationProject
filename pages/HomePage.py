import time

from allure_commons._allure import step
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from infra.config import TestData
from pages.LoginUserPage import LogInUser
from pages.basePage import BasePage



class HomePage(BasePage):


    PLUS_BUTTON_XPATH = '//*[@id="wrapper"]/header/div[1]/ul/li[2]/a/i'
    NEW_PROJECT_XPATH='//a[@aria-label="New project"]'
    SELECT_PROJECT_CLASS_NAME="op-app-menu--item-title"
    SELECT_PROJECT_TEXT="Select a project"
    MENU_PROJECTS_EXPATH='//*[@id="ui-id-1"]'

    #locators for test 10
    SEARCH_PROJECT_BOX_ID="project_autocompletion_input"


    def __init__(self,driver):
        super().__init__(driver)


    #***********************  used to test 9 step 2  ****************************

    @step
    def do_click_green_plus_button(self):
        element=self.get_element_by(By.XPATH,self.PLUS_BUTTON_XPATH)
        self.do_click_by_element(element)
        return True

    def do_click_menu_new_project(self):
        element=self.get_element_by(By.XPATH,self.NEW_PROJECT_XPATH)
        self.do_click_by_element(element)
        return True


    #***********************  used to test 10 step 2  ****************************

    # helper function
    def click_projects_menu(self):
        element=self.get_element_from_list_by_text(By.CLASS_NAME,self.SELECT_PROJECT_CLASS_NAME,self.SELECT_PROJECT_TEXT)
        element.click()

    # helper function
    def type_the_begin_project_test_in_the_search_box(self):
        search_box=self.get_element_by(By.ID,self.SEARCH_PROJECT_BOX_ID)
        self.do_send_key_to_element(search_box,"TestProject1")
        time.sleep(1)

    # helper function
    def choose_specific_project(self,project_name_to_select):
        ul=self.get_element_by(By.XPATH,self.MENU_PROJECTS_EXPATH)
        li_items = ul.find_elements_by_tag_name("li")
        for item in li_items:
            if item.text==project_name_to_select:
                item.click()
                break
    @step
    def choose_specific_project_from_menu_by_name(self,project_name_to_select):
        self.click_projects_menu()
        self.type_the_begin_project_test_in_the_search_box()
        self.choose_specific_project(project_name_to_select)
        return True

















