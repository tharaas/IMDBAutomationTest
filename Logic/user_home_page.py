import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from Infra.base_page import BasePage


class UserHomePage(BasePage):

    USER_NAME = "//span[contains(@class,'ipc-btn__text')]//span[text()='Kakashi']"
    WATCHLIST = "//span[text()='Watchlist']"
    SEARCH_INPUT = "//div[contains(@class,'searchform__inputContainer')]//input[contains(@type,'text')]"
    MENU = "//span[text()='Menu']"

    def __init__(self, driver):
        super().__init__(driver)
        self.user_name = self._driver.find_element(By.XPATH, self.USER_NAME)
        self.watchlist_button = self._driver.find_element(By.XPATH, self.WATCHLIST)
        self.search_input = self._driver.find_element(By.XPATH, self.SEARCH_INPUT)
        self.menu_button = self._driver.find_element(By.XPATH, self.MENU)

    def user_name_is_displayed(self):
        return self.user_name

    def click_on_menu(self):
        self.menu_button.click()

    def click_on_watchlist(self):
        self.watchlist_button.click()

    def click_on_watchlist_is_displayed(self):
        self.click_on_watchlist()
        return self.watchlist_button.is_displayed()

    def click_on_search_input(self, text):
        self.search_input.send_keys(text)

    def press_enter_on_search_input(self):
        self.search_input.send_keys(Keys.RETURN)

    def click_on_search_bar_is_displayed(self):
        self.search_input.click()
        return self.search_input.is_displayed()

    def search_flow(self, text):
        self.search_input.click()
        time.sleep(3)
        self.click_on_search_input(text)
        self.press_enter_on_search_input()
