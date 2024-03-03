import unittest
import concurrent.futures
from Infra.browser_wrapper import BrowserWrapper
from Logic.actor_page import ActorPage
from Logic.attack_in_titan_page import AttackOnTitanPage
from Logic.home_page import HomePage
from Logic.search_options import SearchOptions
from Logic.search_page import SearchPage


class GridTest(unittest.TestCase):
    def setUp(self) -> None:
        self.browser = BrowserWrapper()
        self.cap_list = self.browser.get_cap_list()

    def test_search(self, cap):
        self.driver = self.browser.get_driver_grid(cap)
        self.home_page = HomePage(self.driver)
        self.search = self.browser.get_search_query_url()
        self.home_page.search_flow(self.search)
        self.search_page = SearchPage(self.driver)
        self.search_page.click_on_first_movie_match()
        self.show_page = AttackOnTitanPage(self.driver)
        self.assertTrue(self.show_page.page_title_is_displayed(), "Title is not displayed")

    def test_run_grid_serial_search(self):
        for cap in self.cap_list:
            self.test_search(cap)

    def test_run_grid_parallel_search(self):
        with concurrent.futures.ThreadPoolExecutor(max_workers=len(self.cap_list)) as executer:
            executer.map(self.test_search, self.cap_list)

    def tearDown(self):
        self.driver.quit()


