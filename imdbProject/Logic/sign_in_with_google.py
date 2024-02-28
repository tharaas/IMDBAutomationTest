import time

from selenium.webdriver.common.by import By
from Infra.base_page import BasePage


class SignInWithGoogle(BasePage):

    SIGN_IN_WITH_GOOGLE_LABEL = '//div[text()="Sign in with Google"]'
    EMAIL_INPUT = 'identifierId'
    EMAIL_TXT = "kakashinteam7@gmail.com"
    NEXT_BUTTON = '//span[text()="Next"]'

    def __init__(self, driver):
        super().__init__(driver)
        self.sign_in_with_google_label = self._driver.find_element(By.XPATH, self.SIGN_IN_WITH_GOOGLE_LABEL)
        self.email_input_google = self._driver.find_element(By.ID, self.EMAIL_INPUT)
        self.next_button = self._driver.find_element(By.XPATH, self.NEXT_BUTTON)

    def sign_in_with_google_button_is_displayed(self):
        return self.sign_in_with_google_label.is_displayed()

    def fill_email_input_sign_in_with_google(self):
        self.email_input_google.send_keys(self.EMAIL_TXT)

    def click_next_fill_email_input_input_sign_in_with_google(self):
        self.next_button.click()

    def fill_email_input_and_go_to_password_sign_in_with_google(self):
        self.fill_email_input_sign_in_with_google()
        self.click_next_fill_email_input_input_sign_in_with_google()
        time.sleep(10)
