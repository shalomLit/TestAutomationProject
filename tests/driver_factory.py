import pytest

from infra.config import TestData
from selenium import webdriver


class DriverFactory:
    @staticmethod
    def create_driver():
        driver = webdriver.Chrome(TestData.CHROME_EXECUTABLE_PATH)
        driver.maximize_window()
        return driver
