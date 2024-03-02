import time

from selenium.webdriver.common.by import By
from Infra.base_page import BasePage


class MenuPage(BasePage):

    POPULAR_MOVIES = "//span[text()='Most Popular Movies']"
    MOVIES = "//label[contains(@class,'navlinkcat__item')]//span[text()='Movies']"
    TOPTVSHOWS = "//span[text()='Top 250 TV Shows']"

    def __init__(self, driver):
        super().__init__(driver)
        self.popular_movies = self._driver.find_element(By.XPATH, self.POPULAR_MOVIES)
        self.movies = self._driver.find_element(By.XPATH, self.MOVIES)
        self.top_tv_shows = self._driver.find_element(By.XPATH, self.TOPTVSHOWS)

    def click_on_menu_is_displayed(self):
        return self.movies.is_displayed()

    def click_on_popular_movies(self):
        self.popular_movies.click()

    def click_on_top_tv_shows(self):
        time.sleep(3)
        self.top_tv_shows.click()
