from selenium.webdriver.common.by import By
from Infra.base_page import BasePage


class RemoveFromWatchlist(BasePage):

    WATCHLIST_TITLE = "//div[@class='lister-details']"

    def __init__(self, driver):
        super().__init__(driver)
        self.watchlist_title = self._driver.find_element(By.XPATH, self.WATCHLIST_TITLE)

    def watchlist_page_displayed(self):
        return self.watchlist_title.text

    def is_removing_from_watchlist(self):
        if "0 Titles" == self.watchlist_page_displayed():
            return True
        return False
