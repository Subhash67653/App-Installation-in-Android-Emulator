from appium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = {
    'platformName': 'Android',
    'deviceName': 'emulator-5554',
    'appPackage': 'com.instagram.android',
    'appActivity': 'com.instagram.mainactivity.MainActivity',
}

appium_url = 'http://localhost:4723/wd/hub'
driver = webdriver.Remote(appium_url, desired_caps)
sleep(15)
el8 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText")
el8.send_keys("your username")
#user=driver.find_element(MobileBy.XPATH,"//*[@text='Username']").send_keys('your username')
#password=driver.find_element(MobileBy.XPATH,"//*[@text='Password']").send_keys('Password')
#login=driver.find_element(MobileBy.XPATH,"//*[@text='Log in']").click()
# Enter password
el9 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText")
el9.send_keys("Password")

# Perform login action
el13 = driver.find_element(by=AppiumBy.XPATH, value="//android.view.View[@content-desc=\"Log in\"]")
el13.click()

# Wait for the login process to complete
sleep(5)

# Perform any additional actions after login if needed

# Quit the driver and close the session
driver.quit()
