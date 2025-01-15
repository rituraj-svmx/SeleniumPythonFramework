from selenium.webdriver.common.by import By

from pageObject.Shop import Shop


class HomePage:

    name = (By.XPATH,"//label[text()='Name']/following-sibling::input")
    email = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    password = (By.XPATH, "//label[text()='Password']/following-sibling::input")
    icecreamchbx = (By.XPATH, "//input[@id='exampleCheck1']")
    gender = (By.XPATH, "//label[text()='Gender']/parent::div/select")
    empstatus = (By.XPATH, "//input[@name='inlineRadioOptions']/following-sibling::label[text()='Employed']")
    dob = (By.XPATH, "//label[text()='Date of Birth']/following-sibling::input")
    submit = (By.XPATH, "//input[@type='submit']")
    shopbtn = (By.XPATH, "//a[text()='Shop']")
    successmsg = (By.XPATH, "//div[contains(@class,'alert')]")

    def __init__(self,driver):
        self.driver = driver

    def getname(self):
        return self.driver.find_element(*HomePage.name)

    def getemail(self):
        return self.driver.find_element(*HomePage.email)

    def getpwd(self):
        return self.driver.find_element(*HomePage.password)

    def geticecream(self):
        return self.driver.find_element(*HomePage.icecreamchbx)

    def getgender(self):
        return self.driver.find_element(*HomePage.gender)

    def getemploymentstatus(self):
        return self.driver.find_element(*HomePage.empstatus)

    def getdob(self):
        return self.driver.find_element(*HomePage.dob)

    def submitform(self):
        self.driver.find_element(*HomePage.submit).click()

    def getmsg(self):
        return self.driver.find_element(*HomePage.successmsg)

    def shop_btn(self):
        self.driver.find_element(*HomePage.shopbtn).click()
        shop = Shop(self.driver)
        return shop



