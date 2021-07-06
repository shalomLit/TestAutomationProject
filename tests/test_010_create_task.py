import time

import pytest
from infra.config import TestData
from pages.HomePage import HomePage
from pages.LoginUserPage import LogInUser
from pages.ProjectOverviewPage import ProjectOverview
from pages.workPackagesPage import WorkPackage
from tests.driver_factory import DriverFactory


@pytest.mark.task10
def test_create_task():

        # create a driver
        driver = DriverFactory.create_driver()

        # step 1
        loginUser= LogInUser(driver)  #create a loginuser instance
        loginUser.do_user_login(TestData.MY_USER_NAME,TestData.MY_PASSWORD)

        # step 2
        home_page=HomePage(driver)
        assert home_page.choose_specific_project_from_menu_by_name(TestData.SELECTED_PROJECT) ,"there is a problem with select project from the menu"

        # step 3
        projectOverview = ProjectOverview(driver)
        assert projectOverview.click_on_work_packages_menu_option(), "there is a problem with select 'work package' from the menu"
        # create instance of the next page with the same driver
        workPackage = WorkPackage(driver)
        # note the number of tasks before adding a task
        num_of_tasks = workPackage.total_rows()

        # step 4
        assert workPackage.click_create_task(), "there is a problem with creating new task"

        # step 5
        assert workPackage.vrify_new_task(),"failed to verify the 'new task'"

        # step 6
        assert workPackage.type_into_the_subject_and_description_task(),"there is a problem with typing to the new task"

        # step 7
        assert workPackage.save_task(),"there is a problem with save task"

        # step 8
        num_of_tasks_after_adding_task=workPackage.total_rows()
        assert num_of_tasks+1==num_of_tasks_after_adding_task, "number of tasks before adding +1 need to be te number of tasks after adding"

        # step 9
        last_row_dict=workPackage.vrify_last_row()
        assert last_row_dict["subject"]==TestData.TASK_NAME,f'Expected subject: {TestData.TASK_NAME}'
        assert last_row_dict["type"]=="TASK",f'Expected subject: TASK'





