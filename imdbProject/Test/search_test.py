import time
import unittest
from Infra.browser_wrapper import BrowserWrapper
from Logic.actor_page import ActorPage
from Logic.attack_in_titan_page import AttackOnTitanPage
from Logic.home_page import HomePage
from Logic.search_options import SearchOptions
from Logic.search_page import SearchPage


class IMDBSignInTest(unittest.TestCase):

    def setUp(self):
        self.browser = BrowserWrapper()
        self.driver = self.browser.get_driver()
        self.home_page = HomePage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_search(self):
        self.search = self.browser.get_search_query_url()
        self.home_page.search_flow(self.search)
        self.search_page = SearchPage(self.driver)
        self.search_page.click_on_first_movie_match()
        self.show_page = AttackOnTitanPage(self.driver)
        self.assertTrue(self.show_page.page_title_is_displayed(), "Title is not displayed")

    def test_search_celebs(self):
        self.home_page.click_on_search_option()
        self.search_options = SearchOptions(self.driver)
        self.search_options.click_on_celebs_button()
        self.search = self.browser.get_search_celebs_url()
        self.home_page.search_flow(self.search)
        self.actor_page = ActorPage(self.driver)
        self.assertTrue(self.actor_page.title_is_displayed(), "Title is not displayed")

    def test_thank_you(self):
        time.sleep(15)
        self.search = self.browser.get_thank_you_url()
        self.home_page.search_flow(self.search)
