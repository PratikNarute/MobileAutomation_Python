from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



@staticmethod
def clickAction(self,driver, locator):
    wait = WebDriverWait(driver, 10)
    el = self.driver.find_element(By.XPATH, locator)
    wait.until(EC.element_to_be_clickable(el))
    el.click()

@staticmethod
def sendActon(self, driver, data, locator):
    wait = WebDriverWait(driver,10)
    el = self.driver.find_element(By.XPATH, locator)
    wait.until(EC.visibility_of(el))
    el.send_keys(data)
