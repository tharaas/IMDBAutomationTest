from selenium.webdriver.common.by import By
from Infra.base_page import BasePage


class SignInWithGooglePassword(BasePage):

    PASSWORD_LABEL = '//span[text()="Welcome"]'
    PASSWORD_INPUT = '//input[contains(@type,"password")]'
    NEXT_BUTTON = '//span[text()="Next"]'
    PASSWORD = "Kakashi&Team07"

    def __init__(self, driver):
        super().__init__(driver)
        self.password_label = self._driver.find_element(By.XPATH, self.PASSWORD_LABEL)
        self.password_input = self._driver.find_element(By.XPATH, self.PASSWORD_INPUT)
        self.next_button = self._driver.find_element(By.XPATH, self.NEXT_BUTTON)

    def email_input_and_go_to_password_sign_in_with_google_is_displayed(self):
        return self.password_label

    def fill_password_input_sign_in_with_google(self):
        self.password_input.send_keys(self.PASSWORD)

    def click_on_next_sign_in_with_google(self):
        self.next_button.click()

    def fill_password_input_sign_in_with_google_is_displayed(self):
        return self.password_input

    def flow_password_input_and_click_on_next(self):
        self.fill_password_input_sign_in_with_google()
        self.click_on_next_sign_in_with_google()

