import time
from selenium.webdriver.common.by import By
from Infra.base_page import BasePage


class Rate(BasePage):

    RATE_THIS = "//h6[text()='Rate this']"
    EIGHT_STARS = "//button[@aria-label='Rate 8']"

    def __init__(self, driver):
        super().__init__(driver)
        self.rate_this = self._driver.find_element(By.XPATH, self.RATE_THIS)
        self.eight_stars = self._driver.find_element(By.XPATH, self.EIGHT_STARS)

    def click_on_menu_is_displayed(self):
        time.sleep(2)
        return self.rate_this.is_displayed()

    def click_on_eight_stars_rate(self):
        self.eight_stars.click()
