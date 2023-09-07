from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
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




@staticmethod
def swipeAction(self, driver, start_x, start_y, end_x, end_y ):
    actions = ActionChains(self.driver)
    actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(start_x, start_y)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.move_to_location(end_x, end_y)
    actions.w3c_actions.pointer_action.release()
    actions.perform()
