import unittest
import concurrent.futures
from Infra.browser_wrapper import BrowserWrapper
from Logic.home_page import HomePage
from Logic.sign_in import SignIn
from Logic.sign_in_with_imdb import SignInWithIMDB
from Logic.user_home_page import UserHomePage


class SignInGridTest(unittest.TestCase):
    def setUp(self) -> None:
        self.browser = BrowserWrapper()
        self.cap_list = self.browser.get_cap_list()

    def test_click_on_sign_in_with_imdb_email_flow(self, cap):
        self.driver = self.browser.get_driver_grid(cap)
        self.home_page = HomePage(self.driver)
        self.home_page.click_on_sign_in_button()
        self.sign_in_page = SignIn(self.driver)
        self.sign_in_with_imdb_button = self.sign_in_page.sign_in_with_imdb_button_function()
        self.sign_in_with_imdb = SignInWithIMDB(self.driver)
        self.sign_in_with_imdb.fill_email_and_password_sign_in_with_imdb()
        self.user_home_page = UserHomePage(self.driver)
        self.assertTrue(self.user_home_page.user_name_is_displayed(), "user name is not displayed")

    def test_run_grid_serial_sign_in_with_imdb_email_flow(self):
        for cap in self.cap_list:
            self.test_click_on_sign_in_with_imdb_email_flow(cap)

    def test_run_grid_parallel_sign_in_with_imdb_email_flow(self):
        with concurrent.futures.ThreadPoolExecutor(max_workers=len(self.cap_list)) as executer:
            executer.map(self.test_click_on_sign_in_with_imdb_email_flow, self.cap_list)

    def tearDown(self):
        self.driver.quit()


