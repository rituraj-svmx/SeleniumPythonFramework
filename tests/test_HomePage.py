from datetime import datetime

import pytest

from TestData.test_homepage_data import TestHomePageData
from pageObject.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_submission(self,getData):
        log = self.getlogger()
        homepage = HomePage(self.driver)
        brand = "iphone X"
        assert self.driver.title=="ProtoCommerce","Application is not loaded properly"
        log.info(self.driver.title)
        log.info("firstname is " +getData["firstname"])
        homepage.getname().send_keys(getData["firstname"])
        homepage.getemail().send_keys(getData["email"])
        homepage.getpwd().send_keys("Qwerty@1234")
        if not homepage.geticecream().is_selected():
            homepage.geticecream().click()

        self.select_option_by_text(homepage.getgender(),getData["gender"])
        homepage.getemploymentstatus().click()
        dob = datetime.today().strftime("%d-%m-%Y")
        homepage.getdob().send_keys(dob)
        homepage.submitform()
        alert_text = homepage.getmsg().text
        log.info(alert_text)
        assert ("Success" in alert_text)
        shop = homepage.shop_btn()
        shop.getbrand(brand).click()
        shop.docheckout()
        shop.selectdelloc().send_keys("ind")
        country = self.verify_link_text_presence("India")
        log.info("India is selected as a country")
        country.click()

    @pytest.fixture(params=TestHomePageData.get_testdata("Testcase3"))
    def getData(self,request):
        return request.param






