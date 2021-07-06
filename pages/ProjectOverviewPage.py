from allure_commons._allure import step
from selenium.webdriver.common.by import By

from pages.basePage import BasePage


class ProjectOverview(BasePage):

    MENU_UL_ID="menu-sidebar"
    OPTION_TO_SELECT="Work packages"


    def __init__(self,driver):
        super().__init__(driver)

    #***********************  used to test 10 step 3  ****************************
    @step
    def click_on_work_packages_menu_option(self):
        ul = self.get_element_by(By.ID, self.MENU_UL_ID)
        element=self.find_li_from_ul_by_text(ul,self.OPTION_TO_SELECT)
        self.do_click_by_element(element)
        return True






