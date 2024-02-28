from selenium import webdriver


class browserWrapper():
    def __init__(self):
        self.driver = None
        print("Test start")

    def get_driver(self, url):
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        return self.driver

