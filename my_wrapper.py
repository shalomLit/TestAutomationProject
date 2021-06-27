from telnetlib import EC

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait


class SeleniumWrapper():

    driver:WebDriver

    def get_driver(self,path):
        self.driver= webdriver.Chrome("C:\\Users\\rabi\\Desktop\\chromedriver.exe")
        return self.driver.get(path)

    def do_click(self,element):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME,element)))


    def get_action_chains(self):
        actions=ActionChains(self.driver)
        return actions


    def get_elements_By(self,locator:By,locator_value):
        try:
            return self.driver.find_elements(locator,locator_value)
        except NoSuchElementException as e:
            return None

    def get_element_By(self,locator:By,locator_value):
        try:
            return self.driver.find_element(locator,locator_value)
        except NoSuchElementException as e:
            return None


# 8***************************

    def get_element_by_class_name(self,class_name):
        try:
            return self.driver.find_element_by_class_name(class_name)
        except NoSuchElementException as e:
            return None

    def get_element_by_name(self,name):
        try:
            return self.driver.find_element_by_name(name)
        except NoSuchElementException as e:
            return None

    def get_element_by_xpath(self,xpath):
        try:
            return self.driver.find_element_by_xpath(xpath)
        except NoSuchElementException as e:
            return None

    def get_element_by_id(self,id_text):
        try:
            return self.driver.find_element_by_id(id_text)
        except NoSuchElementException as e:
            return None

    def get_elements_by_class_name(self, class_name):
        try:
            return self.driver.find_elements_by_class_name(class_name)
        except NoSuchElementException as e:
            return None

    def get_elements_by_name(self, name):
        try:
            return self.driver.find_elements_by_name(name)
        except NoSuchElementException as e:
            return None

    def get_elements_by_name(self, xpath):
        try:
            return self.driver.find_elements_by_xpath(xpath)
        except NoSuchElementException as e:
            return None

    def get_element_from_list_by_text(self,locator:By,locator_value,text_to_search:str):
        element_list=self.driver.find_elements(locator,locator_value)
        for element in element_list:
            if text_to_search in element.text:
                return element
        return None

    def get_element_from_list_by_displayed(self,locator:By,locator_value):
        #element_list=self.driver.get_elements_By(locator,locator_value)
        elements_list=self.get_elements_By(locator,locator_value)
        for element in elements_list:
            if element.is_displayed() is True:
                return element
        return None

    def get_element_from_list_by_text_by_class(self,class_text,text_to_search):
        return self.get_element_from_list_by_text(By.CLASS_NAME,class_text,text_to_search)


    def get_element_from_list_by_text_by_id(self,id_text,text_to_search):
        return self.get_element_from_list_by_text(By.ID,id_text,text_to_search)

    def mouse_over_element(self,element:WebElement):
        actions=ActionChains(self.driver)
        actions.move_to_element(element).perform()

    def switch_to_last_opend_tab(self):
        window_handles = self.driver.window_handles
        self.driver.switch_to.window(window_handles[len(window_handles)-1])

    def switch_to_next_opend_tab(self):
        current_window=self.driver.current_window_handle
        window_handles = self.driver.window_handles
        for i in range(len(window_handles)):
            if window_handles[i] is not None:
                if window_handles[i]==current_window:
                   if window_handles[i+1] is not None:
                        self.driver.switch_to.window(window_handles[i+1])








