import unittest
from Infra.browser_wrapper import browserWrapper
from Logic.adding_to_watchlist import AddingToWatchlist
from Logic.attack_in_titan_page import AttackOnTitanPage
from Logic.home_page import HomePage
from Logic.removig_from_watchlist import RemoveFromWatchlist
from Logic.search_page import SearchPage
from Logic.sign_in import SignIn
from Logic.sign_in_with_imdb import SignInWithIMDB
from Logic.user_home_page import UserHomePage
from Logic.watchlist_page import WatchlistPage


class IMDBSignInTest(unittest.TestCase):

    SEARCH_TEXT = "attack in titan"

    def setUp(self):
        self.browser = browserWrapper()
        self.base_url = "https://www.imdb.com/?ref_=nv_home"
        self.driver = self.browser.get_driver(self.base_url)
        self.home_page = HomePage(self.driver)

        self.home_page.click_on_sign_in_button()
        self.sign_in_page = SignIn(self.driver)
        self.sign_in_with_imdb_button = self.sign_in_page.sign_in_with_imdb_button_function()
        self.sign_in_with_imdb = SignInWithIMDB(self.driver)
        self.sign_in_with_imdb.fill_email_and_password_sign_in_with_imdb()
        self.user_home_page = UserHomePage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_add_to_watchlist(self):
        self.user_home_page.search_flow(self.SEARCH_TEXT)
        self.search_page = SearchPage(self.driver)
        self.search_page.click_on_first_movie_match()
        self.show_page = AttackOnTitanPage(self.driver)
        self.show_page.click_on_add_to_watchlist_button()
        self.show_page.go_to_user_home_page()

    def test_check(self):
        self.test_add_to_watchlist()
        self.watchlist_button = AddingToWatchlist(self.driver)
        self.watchlist_button.click_on_watchlist()
        self.watchlist_page = WatchlistPage(self.driver)
        self.assertTrue(self.watchlist_page.is_adding_to_watchlist(), "Watchlist is not displayed")

    def test_removing_from_watchlist(self):
        self.watchlist_button = AddingToWatchlist(self.driver)
        self.watchlist_button.click_on_watchlist()
        self.watchlist_page = WatchlistPage(self.driver)
        self.watchlist_page.removing_from_watchlist()
        self.driver.refresh()
        self.remove = RemoveFromWatchlist(self.driver)
        self.assertTrue(self.remove.is_removing_from_watchlist(), "Watchlist is not displayed")
