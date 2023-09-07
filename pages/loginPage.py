
import utility.excel
from utility import performActions

letStarted_Button = "//android.view.View[@content-desc=\"Get Started\"]"
email_Input = "//android.widget.EditText[@hint='Enter your email']"
password_Input = "//android.widget.EditText[@hint='Enter your password']"
login_Button = "//android.view.View[@content-desc='Login']"

class LoginPage():

    def __init__(self, driver):
        self.driver = driver


    def letStarted(self):
        performActions.clickAction(self,self.driver, letStarted_Button)


    def username(self):
        performActions.clickAction(self, self.driver,email_Input)
        performActions.sendActon(self,self.driver,utility.excel.importData("Sheet", 1,1), email_Input)


    def password(self):
        performActions.clickAction(self, self.driver,password_Input)
        performActions.sendActon(self, self.driver, utility.excel.importData("Sheet", 1,2), password_Input, )

    def clickOnLoginButton(self):
        performActions.clickAction(self,self.driver,login_Button)

    def login(self):
        performActions.clickAction(self, self.driver, letStarted_Button)
        performActions.clickAction(self, self.driver, email_Input)
        performActions.sendActon(self, self.driver, "pratik@kolonizer.com", email_Input)
        performActions.clickAction(self, self.driver, password_Input)
        performActions.sendActon(self, self.driver, "123", password_Input, )
        performActions.clickAction(self,self.driver, login_Button)
