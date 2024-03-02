import time

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Infra.base_page import BasePage


class SearchOptions(BasePage):

    CELEBS_BUTTON = "//span[contains(@class,'li')]//span[text()='Celebs']"

    def __init__(self, driver):
        super().__init__(driver)
        self.celebs_button = self._driver.find_element(By.XPATH, self.CELEBS_BUTTON)

    def click_on_celebs_button(self):
        time.sleep(3)
        element = WebDriverWait(self._driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.CELEBS_BUTTON)))
        if element.is_enabled():
            element.click()
