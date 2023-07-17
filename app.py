from appium import webdriver

desired_caps = {
    'platformName': 'Android',
    'deviceName': 'emulator-5554',
    'app': 'C:\\Users\\dsb67\\Downloads\\instagram-291-1-0-34-111.apk',
    'noReset': True,
    'autoGrantPermissions': True,
    'appPackage': 'com.instagram.android',
    'appActivity': 'com.instagram.mainactivity.MainActivity'
   
}
appium_url = 'http://localhost:4723/wd/hub'

# Replace '4723' with the appropriate Appium server port

driver = webdriver.Remote(appium_url, desired_caps)
  


driver.quit()
