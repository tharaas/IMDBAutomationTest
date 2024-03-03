from selenium.webdriver.common.by import By
from Infra.base_page import BasePage


class AddingToWatchlist(BasePage):

    WATCHLIST_BUTTON = "//span[text()='Watchlist']"

    def __init__(self, driver):
        super().__init__(driver)
        self.watchlist_button = self._driver.find_element(By.XPATH, self.WATCHLIST_BUTTON)

    def click_on_watchlist(self):
        self.watchlist_button.click()

    def click_on_watchlist_is_displayed(self):
        self.click_on_watchlist()
        return self.watchlist_button.is_displayed()
