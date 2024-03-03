from selenium.webdriver.common.by import By
from Infra.base_page import BasePage


class Trailer(BasePage):

    CLOSE = "//span[text()='Close']"
    MUTE = "//div[contains(@aria-label,'Mute button')]"
    FULLSCREEN = "//div[@class='jw-icon jw-icon-inline jw-button-color jw-reset jw-icon-fullscreen']"
    STOP = "//div[@class='jw-icon jw-icon-inline jw-button-color jw-reset jw-icon-playback']"

    def __init__(self, driver):
        super().__init__(driver)
        self.close = self._driver.find_element(By.XPATH, self.CLOSE)
        self.mute = self._driver.find_element(By.XPATH, self.MUTE)
        self.fullscreen = self._driver.find_element(By.XPATH, self.FULLSCREEN)
        self.stop = self._driver.find_element(By.XPATH, self.STOP)

    def movie_page_is_displayed(self):
        return self.close.is_displayed()

    def click_on_close_trailer(self):
        self.close.click()

    def click_on_mute_trailer(self):
        self.mute.click()

    def click_on_fullscreen_trailer(self):
        self.fullscreen.click()

    def click_on_stop_trailer(self):
        self.stop.click()
