from selenium.webdriver.common.by import By
from Infra.base_page import BasePage


class WatchlistPage(BasePage):

    WATCHLIST_TITLE = "//div[@class='lister-details']"
    REMOVE_MARK_FROM_WATCHLIST = "//div[contains(@title,'Click to remove from watchlist')]"

    def __init__(self, driver):
        super().__init__(driver)
        self.watchlist_title = self._driver.find_element(By.XPATH, self.WATCHLIST_TITLE)
        self.remove_mark_from_watchlist = self._driver.find_element(By.XPATH, self.REMOVE_MARK_FROM_WATCHLIST)

    def watchlist_page_displayed(self):
        return self.watchlist_title.text

    def is_adding_to_watchlist(self):
        if "1 Titles" == self.watchlist_page_displayed():
            return True
        return False

    def removing_from_watchlist(self):
        self.remove_mark_from_watchlist.click()

    def is_removing_from_watchlist(self):
        if "0 Titles" == self.watchlist_page_displayed():
            return True
        return False

