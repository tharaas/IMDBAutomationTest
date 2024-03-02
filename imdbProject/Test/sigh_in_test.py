import unittest
import time

from Infra.browser_wrapper import browserWrapper
from Logic.home_page import HomePage
from Logic.sign_in import SignIn
from Logic.sign_in_with_google import SignInWithGoogle
from Logic.sign_in_with_imdb import SignInWithIMDB
from Logic.sign_with_google_password import SignInWithGooglePassword
from Logic.user_home_page import UserHomePage


class IMDBSignInTest(unittest.TestCase):
    def setUp(self):
        self.browser = browserWrapper()
        self.base_url = "https://www.imdb.com/?ref_=nv_home"
        self.driver = self.browser.get_driver(self.base_url)
        self.home_page = HomePage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_click_on_sign_in_with_google_email_flow(self):
        self.home_page.click_on_sign_in_button()
        self.sign_in_page = SignIn(self.driver)
        self.sign_in_with_google_button = self.sign_in_page.sign_in_with_google_button_function()
        self.sign_in_with_google = SignInWithGoogle(self.driver)
        self.sign_in_with_google.fill_email_input_and_go_to_password_sign_in_with_google()
        self.sign_in_with_google_password = SignInWithGooglePassword(self.driver)
        self.sign_in_with_google_password.flow_password_input_and_click_on_next()
        time.sleep(5)
        self.user_home_page = UserHomePage(self.driver)
        self.assertTrue(self.user_home_page.user_name_is_displayed(), "user name is not displayed")

    def test_click_on_sign_in_with_imdb_email_flow(self):
        self.home_page.click_on_sign_in_button()
        self.sign_in_page = SignIn(self.driver)
        self.sign_in_with_imdb_button = self.sign_in_page.sign_in_with_imdb_button_function()
        self.sign_in_with_imdb = SignInWithIMDB(self.driver)
        self.sign_in_with_imdb.fill_email_and_password_sign_in_with_imdb()
        self.user_home_page = UserHomePage(self.driver)
        self.assertTrue(self.user_home_page.user_name_is_displayed(), "user name is not displayed")
