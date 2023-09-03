from time import sleep

import pytest
from self import self
from pages.loginPage import LoginPage

class Test_Login():

    @pytest.fixture(autouse=True)
    def objects(self):
        self.lg = LoginPage(self.driver)

    def test_letStarted(self):
        self.lg.letStarted()

    def test_username(self):
        self.lg.username()

    def test_password(self):
        self.lg.password()

    def test_loginButton(self):
        self.lg.clickOnLoginButton()
