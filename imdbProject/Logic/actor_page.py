from selenium.webdriver.common.by import By
from Infra.base_page import BasePage


class ActorPage(BasePage):

    TITLE = "//h3[text()='People']"

    def __init__(self, driver):
        super().__init__(driver)
        self.title = self._driver.find_element(By.XPATH, self.TITLE)

    def title_is_displayed(self):
        return self.title
