from infra.config import TestData
from pages.HomePage import HomePage
from pages.LoginUserPage import LogInUser
from pages.createProjectPage import CreateProject
from pages.project_page import ProjectPage
import pytest

from tests.driver_factory import DriverFactory


@pytest.mark.task9
def test_create_project():

        # create a driver
        driver = DriverFactory.create_driver()

        # step 1
        loginUser= LogInUser(driver)  #create a loginuser instance
        loginUser.do_user_login(TestData.MY_USER_NAME,TestData.MY_PASSWORD)

        # step 2
        home_page=HomePage(driver)
        click_green_plus_button_status = home_page.do_click_green_plus_button()
        assert click_green_plus_button_status == True, "there is a problem with click plus button"

        assert home_page.do_click_menu_new_project()==True, "there is a problem with click 'new project'"

        createProject = CreateProject(driver) # create an instance of CreateProject

        # step 3
        assert createProject.type_a_unique_value_name(TestData.UNIQUE_VALUE_PROJECT_NAME)==True,"there is a problem with type_a_unique_value_name"

        # step 4
        assert createProject.click_advanced_setting()==True,"there is a problem with click_advanced_setting"

        # step 5
        assert createProject.type_to_description_text_box()==True,"click_advanced_setting type_to_description_text_box"

        # step 7
        assert createProject.select_status()==True, "type_to_description_text_box select_status"

        # step 8
        assert createProject.click_create()== True, "select_status click_create"

        projectPage = ProjectPage(driver)

        # step 9
        corner_page_name_project = projectPage.find_identifire_in_the_page_corner()

        assert (corner_page_name_project == TestData.UNIQUE_VALUE_PROJECT_NAME),\
                f"the project name in the corner is:{corner_page_name_project}" \
                f" and we expected to be{ TestData.UNIQUE_VALUE_PROJECT_NAME}"



        









