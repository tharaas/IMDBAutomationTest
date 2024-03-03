from selenium.webdriver.common.by import By
from Infra.base_page import BasePage


class SearchPage(BasePage):

    TITLES = "//h3[text()='Titles']"
    FIRST_MATCH = "//span[text()='2013–2023']"

    def __init__(self, driver):
        super().__init__(driver)
        self.titles = self._driver.find_element(By.XPATH, self.TITLES)
        self.first_match = self._driver.find_element(By.XPATH, self.FIRST_MATCH)

    def click_on_titles_is_displayed(self):
        return self.titles.is_displayed()

    def click_on_first_movie_match(self):
        self.first_match.click()

