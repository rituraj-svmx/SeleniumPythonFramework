from selenium.webdriver.common.by import By


class Checkout:

    def __init__(self, driver):

        self.driver = driver


    def getcountry(self, country):
        return self.driver.find_element((By.LINK_TEXT, country))