from selenium.webdriver.common.by import By
from Infra.base_page import BasePage


class TopTVShows(BasePage):
    TOP_TV_SHOWS = "//h1[text()='Top 250 TV Shows']"
    RATE = "//button[@aria-label='Rate Breaking Bad']"

    def __init__(self, driver):
        super().__init__(driver)
        self.top_tv_shows = self._driver.find_element(By.XPATH, self.TOP_TV_SHOWS)
        self.rate = self._driver.find_element(By.XPATH, self.RATE)

    def click_on_top_tv_shows_is_displayed(self):
        return self.top_tv_shows.is_displayed()

    def click_on_rate(self):
        self.rate.click()
