import time
import unittest
from Infra.browser_wrapper import BrowserWrapper
from Logic.home_page import HomePage


class IMDBSignInTest(unittest.TestCase):
    def setUp(self):
        self.browser = BrowserWrapper()
        self.driver = self.browser.get_driver()
        self.home_page = HomePage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_instagram_button(self):
        self.instagram_button = self.home_page.wait_for_element_button_and_click(self.home_page.INSTAGRAM_BUTTON)
        time.sleep(5)
        self.url_instagram = self.instagram_button.get_attribute("href")
        print(self.url_instagram)
        self.assertTrue(self.home_page.go_to_instagram_page_is_displayed(self.url_instagram), "url is not displayed")

    def test_youtube_button(self):
        self.youtube_button = self.home_page.wait_for_element_button_and_click(self.home_page.YOUTUBE_BUTTON)
        time.sleep(5)
        self.url_youtube = self.youtube_button.get_attribute("href")
        print(self.url_youtube)
        self.assertTrue(self.home_page.go_to_youtube_page_is_displayed(self.url_youtube), "url is not displayed")
