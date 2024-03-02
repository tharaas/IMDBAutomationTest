from selenium.webdriver.common.by import By
from Infra.base_page import BasePage


class NumberOfRate(BasePage):
    NUMBER_OF_RATE = "//option[text()='Number of ratings']"

    def __init__(self, driver):
        super().__init__(driver)
        self.number_of_rating = self._driver.find_element(By.XPATH, self.NUMBER_OF_RATE)

    def click_on_number_of_rating(self):
        return self.number_of_rating.click()

    def click_on_most_popular_movies_is_displayed(self):
        return self.number_of_rating.is_displayed()
