import unittest
from Infra.browser_wrapper import browserWrapper
from Logic.home_page import HomePage
from Logic.menu_page import MenuPage
from Logic.rate import Rate
from Logic.sign_in import SignIn
from Logic.sign_in_with_imdb import SignInWithIMDB
from Logic.top_tv_shows import TopTVShows
from Logic.user_home_page import UserHomePage


class IMDBSignInTest(unittest.TestCase):

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

    def test_rate(self):
        self.user_home_page.click_on_menu()
        self.menu = MenuPage(self.driver)
        self.menu.click_on_top_tv_shows()
        self.tv_show = TopTVShows(self.driver)
        self.tv_show.click_on_rate()
        self.rate = Rate(self.driver)
        #self.rate.click_on_eight_stars_rate()
        self.assertTrue(self.rate.click_on_menu_is_displayed(), "Rate is not displayed")
