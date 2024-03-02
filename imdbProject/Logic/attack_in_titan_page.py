import time

from selenium.webdriver.common.by import By
from Infra.base_page import BasePage


class AttackOnTitanPage(BasePage):

    PAGE_TITLE = "//span[text()='Attack on Titan']"
    ADD_TO_WATCHLIST_BUTTON = "//div[contains(@class,'sc-491663c0-7 cbGmSP')]//div[contains(@class,'ipc-watchlist-ribbon__icon')]"
    USER_HOME_PAGE = "//a[contains(@class,'sc-dIvsgl cahSX imdb-header__logo-link')]"

    def __init__(self, driver):
        super().__init__(driver)
        self.page_title = self._driver.find_element(By.XPATH, self.PAGE_TITLE)
        self.add_to_watchlist_button = self._driver.find_element(By.XPATH, self.ADD_TO_WATCHLIST_BUTTON)
        self.user_home_page = self._driver.find_element(By.XPATH, self.USER_HOME_PAGE)

    def page_title_is_displayed(self):
        return self.page_title.is_displayed()

    def click_on_add_to_watchlist_button(self):
        time.sleep(2)
        self.add_to_watchlist_button.click()

    def go_to_user_home_page(self):
        self.user_home_page.click()

