from driver import Driver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class BasePage(Driver):
    SEARCH_INPUT = (By.ID, "small-searchterms")

    def find(self, locator):
        return self.driver.find_element(*locator) # metoda find va despacheta toti locatori folosind self.find.

    def click(self, locator):
        self.find(locator).click()  # am creat metoda click folosing metoda find de mai sus

    def type(self, locator, text):
        self.find(locator).send_keys(text)

    def is_element_displayed(self, locator):
        return self.find(locator).is_displayed()

    def get_text(self, locator):
        return self.find(locator).text

    def select_dropdown_option_by_text(self, dropdown_locator, text):
        dropdown_element = self.find(dropdown_locator)
        select = Select(dropdown_element)
        select.select_by_visible_text(text)

    def check_checkbox(self, checkbox_locator):
        checkbox_element = self.find(checkbox_locator)
        if not checkbox_element.is_selected():
            self.click(checkbox_locator)

    def uncheck_check_checkbox(self, checkbox_locator):
        checkbox_element = self.find(checkbox_locator)
        if checkbox_element.is_selected():
            self.click(checkbox_locator)

    def is_url_correct(self, expected_url):
        return expected_url == self.driver.current_url
