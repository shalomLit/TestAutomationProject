# import pytest
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
#
# def step(args):
#     pass
#
#
# class TestOop():
#
#     #before
#     @pytest.fixture
#     def print_hello(self):
#         return "Hello!"
#
#     @pytest.fixture()
#     def print_yeah(self):
#         print("yeah")
#
#     @pytest.fixture
#     def init_web_driver(self):
#         driver = webdriver.Chrome()
#         yield driver
#         print("I'm after yield")
#
#         driver.quit()
#
#     @pytest.mark.sanity
#     def test_my_first_oop(self,print_hello,print_yeah):
#         print(print_hello)
#         print("\nIn oop test!")
#         print("\nafter first assert oop test!")
#         result = True
#         assert result, "Test was failed due to inactive button"
#
#     @pytest.mark.usefixtures("print_yeah")
#     @pytest.mark.selenium
#     def test_my_second_oop_from_first_class(self):
#         print("\nIn second oop test first class")
#
#     @pytest.mark.usefixtures
#     @pytest.mark.homepage
#     @pytest.mark.selenium
#     def test_my_third_oop_from_first_class(self):
#         print("\nIn third oop test first class")
#
#     @step
#     def navigate_to_advantage_shopping(self,driver):
#         driver.get("http://advantageonlineshopping.com/#/")
#
#     @step
#     def wait_for_home_page(self,driver):
#         WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "speakersImg")))
#
#
#     @pytest.mark.selenium2
#     def test_speaker_check(self,init_web_driver):
#         driver = init_web_driver
#
#         self.navigate_to_advantage_shopping(driver)
#         self.wait_for_home_page(driver)
#         speakers_element = driver.find_element_by_id("speakersImg")
#         allure.step("speaker element is ")
#
#         speakers_y = speakers_element.location['y']
#         speakers_x = speakers_element.location['x']
#         speakers_height = speakers_element.size['height']
#         speakers_width = speakers_element.size['width']
#         print("Speaker y: ")
#         laptops_element = driver.find_element_by_id("laptopsImg")
#         laptops_y = laptops_element.location['y']
#         print("Laptop y: ", laptops_y)
#         assert (speakers_y + speakers_height == laptops_y + 1), "Height between lines was incorrect"
#
#
# class TestOopSecond():
#     def test_my_second_oop(self):
#         print("\nIn second oop test")