import time
from telnetlib import EC


from my_wrapper import SeleniumWrapper
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait



class LogInOrganization(SeleniumWrapper):

    organization_locator_name="instance_name"
    input_organization_test="shalomLit"
    submit_locator_xpath='//input[@type="submit"]'

    def __init__(self,path):
        return self.get_driver(path)





    def input_name_organization_and_submit(self):
        input_box_organization = self.get_element_By(By.NAME,self.organization_locator_name)
        input_box_organization.click()
        input_box_organization.send_keys(self.input_organization_test)
        submit_button=self.get_element_By(By.XPATH,self.submit_locator_xpath)


        #WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME,self.submit_locator_name)))
        submit_button.click()




