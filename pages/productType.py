from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
import random
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from utility import performActions

masterMenu_button = "//android.widget.Button[@bounds='[1158,2868][1326,2900]']"
productType_icon = "//android.widget.ImageView[@content-desc='Product Type']"
add_button = "(//android.widget.Button)[3]"
name_input = "(//android.widget.EditText)[1]"
description_input = "(//android.widget.EditText)[2]"
create_button = "//android.widget.Button[@content-desc='Create']"

name = ""
result = False


class ProductType:

    def __init__(self, driver):
        self.driver = driver
        self.randomNumber = random.randint(10, 1000)

    def createProductWithPositiveData(self):
        global name
        performActions.clickAction(self, self.driver, masterMenu_button)
        performActions.swipeAction(self, self.driver, 1095, 2321, 1065, 1595)
        performActions.clickAction(self, self.driver, productType_icon)
        performActions.clickAction(self, self.driver, add_button)
        performActions.clickAction(self, self.driver, name_input)
        performActions.sendActon(self, self.driver, "Product type- " + str(self.randomNumber), name_input)
        performActions.clickAction(self, self.driver, description_input)
        performActions.sendActon(self, self.driver,
                                 "Product type is a group of products which fulfill a similar need for a market segment or market as a whole. Product type can also be defined as set of common specific characteristics in products or goods.",
                                 description_input)
        sleep(3)
        name = self.driver.find_element(By.XPATH, name_input).get_attribute('text')
        performActions.clickAction(self, self.driver, create_button)

    def to_check_that_impact_of_created_product_type_on_the_table_list(self, data):
        global result
        print("Name of product type:", data)
        try:  # Exception code we write here
            result = self.driver.find_element(By.XPATH,
                                              "//android.view.View[@content-desc='" + data + "']").is_displayed()

        except Exception as e:  # solution for exception (exception handling code) here
            assert True

        assert result == True
