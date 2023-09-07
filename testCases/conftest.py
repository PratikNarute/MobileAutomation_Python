from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy


@pytest.fixture(scope="class", autouse=True)
def setup(request):
    global driver
    capabilities = dict(
        platformName='Android',
        automationName='uiautomator2',
        deviceName='Pratik_Android',
        app= 'C:\\Users\\Lenovo\\Desktop\\Automation_Python\\Appium_Python\\TestData\\Pratik.apk',

        # appPackage='com.android.settings',
        # appActivity='.Settings',
        language='en',
        locale='US'
    )
    appium_server_url = 'http://localhost:4723'
    driver = webdriver.Remote(appium_server_url, capabilities)
    request.cls.driver = driver
    return driver


@pytest.fixture(scope="function", autouse=True)
def wait(request):
    driver.implicitly_wait(15)



def pytest_html_report_title(report):
    report.title = "CRM"


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call':
        feature_request = item.funcargs['request']
        extra.append(pytest_html.extras.url('http://devdreamcity.kolonizer.in/login'))
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            driver.get_screenshot_as_file('C:\\Users\\Lenovo\\Desktop\\Automation_Python\\Appium_Python\\Screenshots\\failed.png')
            extra.append(pytest_html.extras.image('C:\\Users\\Lenovo\\Desktop\\Automation_Python\\Appium_Python\\Screenshots\\failed.png'))
            extra.append(pytest_html.extras.html('<div>Additional HTML</div>'))
        report.extra = extra

