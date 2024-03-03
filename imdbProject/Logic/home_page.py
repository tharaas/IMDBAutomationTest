import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from Infra.base_page import BasePage


class HomePage(BasePage):

    MENU = "//span[text()='Menu']"
    SING_IN_BUTTON = "//div[contains(@class,'nav__userMenu')]/a//span[text()='Sign In']"
    LANGUAGE_BUTTON = "//span[text()='EN']"
    FRANCE_LANGUAGE = "//span//span[text()='Français (France)']"
    SEARCH_INPUT = "//div[contains(@class,'searchform__inputContainer')]//input[contains(@type,'text')]"
    SEARCH_OPTION = "//div[contains(@class,'sc-lmgPJu cvbxBC')]"
    CELEBS_BUTTON = "//span[contains(@class,'li')]//span[text()='Celebs']"
    INSTAGRAM_BUTTON = "//a[contains(@title,'Instagram')]"
    YOUTUBE_BUTTON = "//a[contains(@title,'YouTube')]"
    BROWSE_TRAILERS = "//a[text()='Browse trailers']"

    def __init__(self, driver):
        super().__init__(driver)
        self.menu_button = self._driver.find_element(By.XPATH, self.MENU)
        self.sign_in_button = self._driver.find_element(By.XPATH, self.SING_IN_BUTTON)
        self.language_button = self._driver.find_element(By.XPATH, self.LANGUAGE_BUTTON)
        self.france_language = self._driver.find_element(By.XPATH, self.FRANCE_LANGUAGE)
        self.search_input = self._driver.find_element(By.XPATH, self.SEARCH_INPUT)
        self.search_option = self._driver.find_element(By.XPATH, self.SEARCH_OPTION)
        self.celebs_button = self._driver.find_element(By.XPATH, self.CELEBS_BUTTON)
        self.browse_trailers = self._driver.find_element(By.XPATH, self.BROWSE_TRAILERS)

        self.INSTAGRAM_BUTTON = (By.XPATH, self.INSTAGRAM_BUTTON)
        self.wait = WebDriverWait(driver, 10)
        self.YOUTUBE_BUTTON = (By.XPATH, self.YOUTUBE_BUTTON)

    def click_on_menu(self):
        self.menu_button.click()

    def click_on_sign_in_button(self):
        self.sign_in_button.click()

    def click_on_language_button(self):
        self.language_button.click()

    def click_on_france_language_button(self):
        self.france_language.click()

    def click_on_change_language_from_english_to_france_button(self):
        self.click_on_language_button()
        self.click_on_france_language_button()

    def click_on_search_option(self):
        self.search_option.click()

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

    def wait_for_element_button_and_click(self, locator):
        self.scrollHeight()
        self.scrollHeight()
        self.scrollHeight()
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
        return element

    def scrollHeight(self):
        self._driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)

    def go_to_instagram_page_is_displayed(self, url):
        if url == "https://instagram.com/imdb":
            return True
        return False

    def go_to_youtube_page_is_displayed(self, url):
        if url == "https://youtube.com/imdb/":
            return True
        return False

    def click_on_browse_trailers(self):
        self.browse_trailers.click()
