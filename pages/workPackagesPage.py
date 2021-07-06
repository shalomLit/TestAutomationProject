import time

from selenium.webdriver.common.by import By
from allure_commons._allure import step
from infra.config import TestData
from pages.basePage import BasePage


class WorkPackage(BasePage):


    WORK_PACAGES_TABEL_CLASS="results-tbody"
    PAGES_OF_TASKS_CLASS="pagination--items"
    CREATE_BUTTON_CLASS="wp-create-button"
    UL_DROPDOWN_MENU="dropdown-menu"
    NEW_DIV_XPATH='//span[@class="inline-edit--display-field status -required -editable"]'
    TASK_DIV_XPATH='//span[@title="Task"]'
    TASK_NAME_ID="wp-new-inline-edit--field-subject"
    TASK_DESCRIPTION_CLASS="op-uc-p"
    LAST_ROW_SUBJECT_CLASS_NAME="wp-table--cell-container inline-edit--container subject"
    LAST_ROW_SUBJECT_XPATH='//*[@title="sholit test"]'
    LAST_ROW_TYPE_XPATH='//*[@title = "Task"]'
    SAVE_BUTTON_ID_TASK="work-packages--edit-actions-save"
    SAVE_BUTTON_XPATH_TASK='//*[@id="work-packages--edit-actions-save"]'
    TOTAL_ROWS_CLASS_NAME="pagination--range"
    DIV_NEXT_TABLE_PAGE_CLASS_NAME="pagination--pages"
    TABLE_CLASS_NAME="results-tbody"



    def __init__(self,driver):
        super().__init__(driver)

    #***********************  used to step 4  ****************************

    # helper function
    def click_create(self):
        create_button=self.get_element_by(By.CLASS_NAME,self.CREATE_BUTTON_CLASS)
        time.sleep(1)
        self.do_click_by_element(create_button)

    # helper function
    def select_task_from_dropdown_create_menu(self):
        dropdown_menu_list=self.get_element_by(By.CLASS_NAME,self.UL_DROPDOWN_MENU)
        task_element=self.find_li_from_ul_by_text(dropdown_menu_list,"TASK")
        task_element.click()

    @step
    def click_create_task(self):
        self.click_create()
        self.select_task_from_dropdown_create_menu()
        return True

    #***********************  used to step 5  ****************************

    @step
    def vrify_new_task(self):
        new_element_div=self.get_element_by(By.XPATH,self.NEW_DIV_XPATH)
        task_element_div=self.get_element_by(By.XPATH,self.TASK_DIV_XPATH)
        return self.is_displayed(new_element_div) and self.is_displayed(task_element_div)



    #***********************  used to step 6  ****************************

    # helper function
    def type_task_name(self):
        task_name_element=self.get_element_by(By.ID,self.TASK_NAME_ID)
        self.do_send_key_to_element(task_name_element,TestData.TASK_NAME)

    # helper function
    def type_task_description(self):
        task_description_element=self.get_element_by(By.CLASS_NAME,self.TASK_DESCRIPTION_CLASS)
        self.actions.move_to_element(task_description_element).click(task_description_element).perform()
        self.do_send_key_to_element(task_description_element,TestData.TASK_DESCRIPTION)

    @step
    def type_into_the_subject_and_description_task(self):
        self.type_task_name()
        self.type_task_description()
        return True



    #***********************  used to step 7  ****************************

    @step
    def save_task(self):
        button=self.get_element_by(By.ID,self.SAVE_BUTTON_ID_TASK)
        self.driver.execute_script("arguments[0].scrollIntoView();",button)
        self.do_click_by_element(button)
        time.sleep(2)
        return True


    #***********************  used to step 8  ****************************

    # def rows_table_count(self):
    #     table=self.get_element_by(By.CLASS_NAME,self.WORK_PACAGES_TABEL_CLASS)
    #     number_of_rows=self.get_number_of_sub_tags_by_tag_element(table,"tr")
    #     return number_of_rows
    @step
    def total_rows(self):
        total_element=self.get_element_by(By.CLASS_NAME,self.TOTAL_ROWS_CLASS_NAME)
        self.driver.execute_script("arguments[0].scrollIntoView();",total_element)
        return int(total_element.text.split()[2].split("/")[1].split(")")[0])




    #***********************  TEST 10 step 9  ****************************
    # helper function
    def click_last_table_page(self):
        div_nexts=self.get_element_clickable(By.CLASS_NAME,self.DIV_NEXT_TABLE_PAGE_CLASS_NAME)
        list_a=div_nexts.find_elements_by_tag_name("a")
        element=list_a[len(list_a) - 2]
        self.driver.execute_script("arguments[0].scrollIntoView();",element)
        self.do_click_by_element(element)

    @step
    def vrify_last_row(self):
        self.click_last_table_page()
        table=self.get_element_by(By.CLASS_NAME,self.TABLE_CLASS_NAME)
        all_rows_in_table=table.find_elements_by_tag_name("tr")
        last_row=all_rows_in_table[len(table.find_elements_by_tag_name("tr"))-1]
        all_td_in_last_row=last_row.find_elements_by_tag_name("td")
        return {
            "subject":all_td_in_last_row[2].text,
            "type":all_td_in_last_row[3].text
        }







