from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from time import sleep


class Add_Remove(BasePage):
    LINK = "https://the-internet.herokuapp.com/add_remove_elements/"

    ADD_ELEMENT = (By.XPATH, "//button[@onclick='addElement()']")
    REMOVE_ELEMENT = (By.XPATH, "//button[@onclick='deleteElement()']")

    def navigate_page(self):
        self.driver.get(self.LINK)

    def add_elem(self):
        self.find(self.ADD_ELEMENT).click()
        sleep(3)

    def delete_element(self):
        self.find(self.REMOVE_ELEMENT).click()
        sleep(3)
