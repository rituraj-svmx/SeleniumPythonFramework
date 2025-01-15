from selenium.webdriver.common.by import By


class UploadFile:

    download = (By.CSS_SELECTOR,"#downloadButton")
    choose_file = (By.CSS_SELECTOR, "input[type='file']")
    toast_locator = (By.CSS_SELECTOR, ".Toastify__toast-body div:nth-child(2)")
    price = (By.XPATH,"//div[text()='Apple']/parent::div//following-sibling::div[@data-column-id='4']/child::div")


    def __init__(self,driver):
        self.driver = driver

    def download_file(self):
        return self.driver.find_element(*UploadFile.download)

    def upload_file(self):
        return self.driver.find_element(*UploadFile.choose_file)

    def toast_msg(self):
        return self.driver.find_element(*UploadFile.toast_locator)
