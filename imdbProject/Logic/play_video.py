from selenium.webdriver.common.by import By
from Infra.base_page import BasePage


class PlayVideo(BasePage):

    MOVIE_PAGE = "//h1/span[text()='The Gentlemen']"
    TRAILER = "//div[contains(@class,'sc-491663c0-8 chDPzy')]"

    def __init__(self, driver):
        super().__init__(driver)
        self.movie_page = self._driver.find_element(By.XPATH, self.MOVIE_PAGE)
        self.trailer = self._driver.find_element(By.XPATH, self.TRAILER)

    def movie_page_is_displayed(self):
        return self.movie_page.is_displayed()

    def click_on_play_trailer(self):
        self.trailer.click()

