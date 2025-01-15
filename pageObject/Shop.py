from selenium.webdriver.common.by import By


class Shop:

    checkoutbtn = (By.XPATH,"//a[contains(text(),'Checkout')]")
    checkout = (By.XPATH, "//button[contains(text(), 'Checkout')]")
    dellocation = (By.XPATH,"//input[@id='country']")



    def __init__(self, driver):
        self.driver = driver

    def getbrand(self,brand):
        return self.driver.find_element(By.XPATH,f"//app-card-list[@class='row']//a[text()='{brand}']//parent::h4/parent::div//following-sibling::div/button")

    def docheckout(self):
        self.driver.find_element(*Shop.checkoutbtn).click()
        self.driver.find_element(*Shop.checkout).click()

    def selectdelloc(self):
        return self.driver.find_element(*Shop.dellocation)
