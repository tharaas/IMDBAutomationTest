from selenium.webdriver.common.by import By
from Infra.base_page import BasePage


class SignIn(BasePage):

    SIGN_IN_LABEL = '//h1[text()="Sign in"]'
    SIGN_IN_WITH_GOOGLE_BUTTON = '//span[text()="Sign in with Google"]'

    def __init__(self, driver):
        super().__init__(driver)
        self.sign_in_label = self._driver.find_element(By.XPATH, self.SIGN_IN_LABEL)
        self.sign_in_with_google_button = self._driver.find_element(By.XPATH, self.SIGN_IN_WITH_GOOGLE_BUTTON)

    def sign_in_label_is_displayed(self):
        return self.sign_in_label.is_displayed()

    def sign_in_with_google_button_function(self):
        self.sign_in_with_google_button.click()
