from selenium.webdriver.common.by import By
from Infra.base_page import BasePage


class BrowserTrailers(BasePage):

    MOVIE_NAME = "//a[text()='The Gentlemen']"

    def __init__(self, driver):
        super().__init__(driver)
        self.movie_name = self._driver.find_element(By.XPATH, self.MOVIE_NAME)

    def click_on_movie(self):
        self.movie_name.click()
