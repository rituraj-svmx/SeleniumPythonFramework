import inspect
import logging
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class BaseClass:

    def getlogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        filename = logging.FileHandler("../utilities/logfile.log")
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s) : %(message)s")
        filename.setFormatter(formatter)
        logger.addHandler(filename)
        logger.setLevel(logging.DEBUG)
        return logger

    def verify_link_text_presence(self, text):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, text)))
        return element

    def select_option_by_text(self, locator, text):
        sel = Select(locator)
        sel.select_by_visible_text(text)

    def verify_toast_message(self,locator):
        wait = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
