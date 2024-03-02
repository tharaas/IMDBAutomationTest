from selenium.webdriver.common.by import By
from Infra.base_page import BasePage


class PopularMovies(BasePage):
    MOST_POPULAR_MOVIES = "//h1[text()='Most Popular Movies']"
    MYSTERY_POPULAR_MOVIES = "//span[text()='Mystery']"
    SORT_BY = "//select[contains(@class,'ipc-simple-select__input')]"

    def __init__(self, driver):
        super().__init__(driver)
        self.most_popular_movies = self._driver.find_element(By.XPATH, self.MOST_POPULAR_MOVIES)
        self.sort_by = self._driver.find_element(By.XPATH, self.SORT_BY)

    def click_on_most_popular_movies_is_displayed(self):
        return self.most_popular_movies.is_displayed()

    def click_on_sort_by(self):
        self.sort_by.click()
