from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By

from Infra.base_page import BasePage


class UserHomePage(BasePage):

    USER_NAME = "//span[contains(@class,'ipc-btn__text')]//span[text()='Kakashi']"
    SEARCH_BAR = 'nav-search-form'
    MENU = 'imdbHeader-navDrawerOpen'

    def __init__(self, driver):
        super().__init__(driver)
        self.user_name = self._driver.find_element(By.XPATH, self.USER_NAME)
        self.search_bar = self._driver.find_element(By.ID, self.SEARCH_BAR)
        self.menu_button = self._driver.find_element(By.ID, self.MENU)

    def user_name_is_displayed(self):
        return self.user_name

    def click_on_search_bar(self):
        self.search_bar.click()

    def is_click_on_search_bar(self):
        self.click_on_search_bar()
        return self.search_bar.is_displayed()

    def click_on_menu(self):
        self.menu_button.click()

    def is_click_on_menu(self):
        self.click_on_menu()
        return self.menu_button.is_displayed()
