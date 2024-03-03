import json
from selenium import webdriver


class BrowserWrapper:
    def __init__(self):
        self.driver = None
        print('test has started')

    def get_json_file(self):
        with open("../infra/config.json", "r") as f:
            config = json.load(f)
        return config

    def get_hub_url(self):
        self.json = self.get_json_file()
        return self.json["hub"]

    def get_search_query_url(self):
        self.json = self.get_json_file()
        return self.json["search_query"]

    def get_search_celebs_url(self):
        self.json = self.get_json_file()
        return self.json["search_celebs"]

    def get_thank_you_url(self):
        self.json = self.get_json_file()
        return self.json["THANK_YOU"]

    def get_driver(self, website_url="https://www.imdb.com/?ref_=nv_home"):
        self.driver = webdriver.Chrome()
        self.driver.get(website_url)
        return self.driver

    def get_driver_grid(self, cap, website_url="https://www.imdb.com/?ref_=nv_home"):
        self.url_hub = self.get_hub_url()
        self.driver = webdriver.Remote(command_executor=self.url_hub, options=cap)
        self.driver.get(website_url)
        return self.driver

    def get_cap_list(self):
        self.json = self.get_json_file()

        if "capabilities" not in self.json:
            raise ValueError("Missing 'capabilities' configuration in config.json")

        for browser in self.json["capabilities"]:
            if browser["browserName"] == "chrome":
                self.options_chrome = webdriver.ChromeOptions()
                self.options_chrome.add_argument('--platform=MAC')

            elif browser["browserName"] == "firefox":
                self.options_firefox = webdriver.FirefoxOptions()
                self.options_firefox.add_argument('--platform=MAC')

            #elif browser["browserName"] == "safari":
                #self.options_safari = webdriver.SafariOptions()
                #self.options_safari.add_argument('--platform=MAC')
            else:
                raise ValueError(f"Unsupported browser: {browser['browserName']}")

        cap_list = [self.options_chrome, self.options_firefox]
        print(cap_list)
        return cap_list

    def get_teardown(self):
        self.driver.quit()
