import time
import unittest
from Infra.browser_wrapper import browserWrapper
from Logic.home_page import HomePage
from Logic.menu_page import MenuPage
from Logic.number_of_ratings import NumberOfRate
from Logic.popular_movies import PopularMovies


class IMDBSignInTest(unittest.TestCase):
    def setUp(self):
        self.browser = browserWrapper()
        self.base_url = "https://www.imdb.com/?ref_=nv_home"
        self.driver = self.browser.get_driver(self.base_url)
        self.home_page = HomePage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_popular_mystery_movies(self):
        self.home_page.click_on_menu()
        time.sleep(3)
        self.menu = MenuPage(self.driver)
        self.menu.click_on_popular_movies()
        self.popular_movies = PopularMovies(self.driver)
        self.sort_by = self.popular_movies.click_on_sort_by()
        self.number_of_rate = NumberOfRate(self.driver)
        self.number_of_rate.click_on_number_of_rating()
        self.assertTrue(self.number_of_rate.click_on_most_popular_movies_is_displayed(), "Sort is not displayed")
