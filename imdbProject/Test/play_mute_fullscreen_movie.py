import time
import unittest
from Infra.browser_wrapper import browserWrapper
from Logic.browse_trailers import BrowserTrailers
from Logic.home_page import HomePage
from Logic.play_video import PlayVideo
from Logic.trailer import Trailer


class IMDBSignInTest(unittest.TestCase):

    def setUp(self):
        self.browser = browserWrapper()
        self.base_url = "https://www.imdb.com/?ref_=nv_home"
        self.driver = self.browser.get_driver(self.base_url)
        self.home_page = HomePage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_play_a_browse_trailer(self):
        self.home_page.click_on_browse_trailers()
        self.browse_trailers = BrowserTrailers(self.driver)
        self.browse_trailers.click_on_movie()
        self.play_video = PlayVideo(self.driver)
        self.play_video.click_on_play_trailer()
        self.trailer = Trailer(self.driver)
        self.assertTrue(self.trailer.movie_page_is_displayed(), "Video is not displayed")

    def test_mute_a_browse_trailer(self):
        self.home_page.click_on_browse_trailers()
        self.browse_trailers = BrowserTrailers(self.driver)
        self.browse_trailers.click_on_movie()
        self.play_video = PlayVideo(self.driver)
        self.play_video.click_on_play_trailer()
        self.trailer = Trailer(self.driver)
        self.trailer.click_on_mute_trailer()
        time.sleep(2)
        self.assertTrue(self.trailer.movie_page_is_displayed(), "Mute Video is not displayed")

    def test_fullscreen_a_browse_trailer(self):
        self.home_page.click_on_browse_trailers()
        self.browse_trailers = BrowserTrailers(self.driver)
        self.browse_trailers.click_on_movie()
        self.play_video = PlayVideo(self.driver)
        self.play_video.click_on_play_trailer()
        self.trailer = Trailer(self.driver)
        self.trailer.click_on_fullscreen_trailer()
        time.sleep(2)
        self.assertTrue(self.trailer.movie_page_is_displayed(), "Fullscreen is not displayed")

    def test_stop_a_browse_trailer(self):
        self.home_page.click_on_browse_trailers()
        self.browse_trailers = BrowserTrailers(self.driver)
        self.browse_trailers.click_on_movie()
        self.play_video = PlayVideo(self.driver)
        self.play_video.click_on_play_trailer()
        self.trailer = Trailer(self.driver)
        self.trailer.click_on_stop_trailer()
        time.sleep(2)
        self.assertTrue(self.trailer.movie_page_is_displayed(), "Stop video is not displayed")
