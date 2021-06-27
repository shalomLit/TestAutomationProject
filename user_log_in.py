from my_wrapper import SeleniumWrapper
from selenium.webdriver.common.by import By


class UserLogIn(SeleniumWrapper):

    userName_locator_id="username"
    password_locator_id="password"
    my_user_name="shdover0@gmail.com"
    my_password="Sholit3100"
    submit_locator_name="login"
    submit_locator_xpath='//input[@type="submit" and @value="Sign in" and @value="Sign in"]'




    def __init__(self,path):
        return self.get_driver(path)


    def log_in(self):
        actions=self.get_action_chains()
        userName_element=self.get_element_By(By.ID,self.userName_locator_id)
        password_element=self.get_element_By(By.ID,self.password_locator_id)
        #submit_button=self.get_elements_By(By.NAME,self.submit_locator_name)

        submit_button=self.get_element_from_list_by_displayed(By.NAME,self.submit_locator_name)

        actions.move_to_element(userName_element).click().send_keys(self.my_user_name)
        actions.move_to_element(password_element).click().send_keys(self.my_password).perform()
        submit_button.click()







