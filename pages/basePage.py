from telnetlib import EC
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class BasePage:

    driver:WebDriver
    actions:WebDriver

    def __init__(self,driver,LOGIN_URL):
        self.driver=driver
        self.driver.get(LOGIN_URL)
        self.driver.maximize_window()


    def mouse_over_element(self,element:WebElement):
        self.actions.move_to_element(element).perform()


    def get_elements_by(self,locator:By,locator_value):
        try:
            element_list= self.driver.find_elements(locator,locator_value)
            return element_list
        except NoSuchElementException as e:
            return None

    def get_element_from_list_by_text(self, locator: By, locator_value, text_to_search: str):
        try:
            element_list = self.driver.find_elements(locator, locator_value)
            for element in element_list:
                if text_to_search in element.text:
                    return element
        except NoSuchElementException as e:
            return None



    def get_element_by(self,locator:By,locator_value):

        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((locator, locator_value)))
        element= self.driver.find_element(locator,locator_value)
        return element

    def is_displayed(self,element):

        return element.is_displayed()





    def click_on_element_displayed_from_a_list_of_elements(self,elements):
        for element in elements:
            if element.is_displayed() is True:
                element.click()
        return None


    def do_click_by_locator(self,by_locator):
        print("do click basePage")
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def do_click_by_element(self,element:WebDriver):

        if element.is_displayed()==True:
            element.click()
            return True
        else:
            return False


    def do_send_key(self,by_locator,text):
        try:
            print("do_send_key basePage")
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

        except NoSuchElementException as e:
            return None

    def do_send_key_to_element(self,element,text):
        try:
            element.send_keys(text)
            return True

        except NoSuchElementException as e:
            return None











