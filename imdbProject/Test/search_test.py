import unittest
from Infra.browser_wrapper import browserWrapper
from Logic.attack_in_titan_page import AttackOnTitanPage
from Logic.home_page import HomePage
from Logic.search_options import SearchOptions
from Logic.search_page import SearchPage


class IMDBSignInTest(unittest.TestCase):
    SEARCH_TEXT = "attack in titan"
    SEARCH_CELEBS = "austin butler"

    def setUp(self):
        self.browser = browserWrapper()
        self.base_url = "https://www.imdb.com/?ref_=nv_home"
        self.driver = self.browser.get_driver(self.base_url)
        self.home_page = HomePage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_search(self):
        self.home_page.search_flow(self.SEARCH_TEXT)
        self.search_page = SearchPage(self.driver)
        self.search_page.click_on_first_movie_match()
        self.show_page = AttackOnTitanPage(self.driver)
        self.assertTrue(self.show_page.page_title_is_displayed(), "Label is not displayed")

    def test_search_celebs(self):
        self.home_page.click_on_search_option()
        self.search_options = SearchOptions(self.driver)
        #self.search_options.click_on_celebs_button()
        #self.home_page.search_flow(self.SEARCH_CELEBS)
        #self.search_page = SearchPage(self.driver)
        #self.search_page.click_on_first_movie_match()
        #self.show_page = AttackOnTitanPage(self.driver)
        #self.show_page.click_on_add_to_watchlist_button()
        #self.assertTrue(self.show_page.page_title_is_displayed(), "Label is not displayed")