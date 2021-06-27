import pytest
from selenium import webdriver
from infra.config import TestData


@pytest.fixture(scope='class')
def init_driver(request):
    print("init driver before yield")
    web_driver=webdriver.Chrome(TestData.CHROME_EXECUTABLE_PATH)
    request.cls.driver=web_driver
    yield
    print("init driver apter yield")
   # web_driver.close()