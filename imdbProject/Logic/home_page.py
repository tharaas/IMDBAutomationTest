from selenium.webdriver.common.by import By
from Infra.base_page import BasePage


class HomePage(BasePage):

    SING_IN_BUTTON = "//div[contains(@class,'nav__userMenu')]/a//span[text()='Sign In']"

    def __init__(self, driver):
        super().__init__(driver)
        self.sign_in_button = self._driver.find_element(By.XPATH, self.SING_IN_BUTTON)

    def click_on_sign_in_button(self):
        self.sign_in_button.click()
