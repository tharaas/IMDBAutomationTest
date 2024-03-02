import time

from selenium.webdriver.common.by import By
from Infra.base_page import BasePage


class SignInWithIMDB(BasePage):

    SIGN_IN_WITH_IMDB_LABEL = '//h1[contains(@class,"a-spacing-small")]'
    EMAIL_INPUT = '//input[@id="ap_email"]'
    EMAIL_TXT = "kakashinteam7@gmail.com"
    PASSWORD_INPUT = '//input[contains(@type,"password")]'
    PASSWORD = "Kakashi&Team07"
    SIGN_IN_BUTTON = 'signInSubmit'

    def __init__(self, driver):
        super().__init__(driver)
        self.sign_in_with_imdb_label = self._driver.find_element(By.XPATH, self.SIGN_IN_WITH_IMDB_LABEL)
        self.email_input_imdb = self._driver.find_element(By.XPATH, self.EMAIL_INPUT)
        self.password_input = self._driver.find_element(By.XPATH, self.PASSWORD_INPUT)
        self.sign_in_button = self._driver.find_element(By.ID, self.SIGN_IN_BUTTON)

    def sign_in_with_imdb_button_is_displayed(self):
        return self.sign_in_with_imdb_label.is_displayed()

    def fill_email_input_sign_in_with_imdb(self):
        self.email_input_imdb.send_keys(self.EMAIL_TXT)

    def fill_password_input_sign_in_with_imdb(self):
        self.password_input.send_keys(self.PASSWORD)

    def click_on_sign_in_with_imdb(self):
        self.sign_in_button.click()

    def fill_email_and_password_sign_in_with_imdb(self):
        self.fill_email_input_sign_in_with_imdb()
        self.fill_password_input_sign_in_with_imdb()
        self.click_on_sign_in_with_imdb()
