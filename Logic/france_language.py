from selenium.webdriver.common.by import By
from Infra.base_page import BasePage


class FranceLanguage(BasePage):

    FRANCE_BUTTON = "//span[text()='FR']"

    def __init__(self, driver):
        super().__init__(driver)
        self.france_button = self._driver.find_element(By.XPATH, self.FRANCE_BUTTON)

    def change_language_is_displayed(self):
        return self.france_button.is_displayed()
