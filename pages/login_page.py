from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    LOGIN_PAGE_URL = "https://demo.nopcommerce.com/login"
    EMAIL_INPUT = (By.ID, "Email")
    PASSWORD_INPUT = (By.ID, "Password")
    LOGIN_BUTTON = (By.CLASS_NAME, "login-button")

    ERROR_MESSAGE_MAIN = (By.CSS_SELECTOR, "div.message-error")
    ERROR_MESSAGE_EMAIL = (By.ID, "Email-error")

    def navigate_to_login_page(self):
        self.driver.get(self.LOGIN_PAGE_URL)

    def set_email(self, email):
        # self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)
        self.type(self.EMAIL_INPUT, email) # nu mai despachetam cu * pt e despachetat in base_page in metoda find

    def set_password(self, password):
        # self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.type(self.PASSWORD_INPUT, password)

    def click_login_button(self):
        # self.driver.find_element(*self.LOGIN_BUTTON).click()
        self.click(self.LOGIN_BUTTON)

    def is_main_error_message_displayed(self):
        # return self.driver.find_element(*self.ERROR_MESSAGE_MAIN).is_displayed()
        # return self.find(self.ERROR_MESSAGE_MAIN).is_displayed()
        return self.is_element_displayed(self.ERROR_MESSAGE_MAIN)
        # returneaza True daca este afisat si False daca nu este afisat

    def get_main_error_message_text(self):
        # return self.find(self.ERROR_MESSAGE_MAIN).text
        return self.get_text(self.ERROR_MESSAGE_MAIN)

    def is_email_error_message_displayed(self):
        return self.is_element_displayed(self.ERROR_MESSAGE_EMAIL)
        # returneaza True daca este afisat si False daca nu este afisat

    def get_email_error_message_text(self):
        return self.get_text(self.ERROR_MESSAGE_EMAIL)
