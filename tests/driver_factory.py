from selenium import webdriver
from infra.ui.config import TestData


class DriverFactory:
    @staticmethod
    def create_driver():
        driver = webdriver.Chrome(TestData.CHROME_EXECUTABLE_PATH)
        driver.maximize_window()
        return driver
