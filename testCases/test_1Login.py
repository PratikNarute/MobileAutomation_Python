from time import sleep

import pytest
from self import self
from pages.loginPage import LoginPage
from testCases import conftest


class Test_Login():

    @pytest.fixture(autouse=True)
    def objects(self):
        self.lg = LoginPage(self.driver)


    def test_login_with_valid_credentials(self):
        self.lg.letStarted()
        self.lg.username()
        self.lg.password()
        self.lg.clickOnLoginButton()
        sleep(6)









