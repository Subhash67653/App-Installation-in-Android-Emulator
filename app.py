from appium import webdriver



desired_caps = {
    'platformName': 'Android',
    'deviceName': 'emulator-5554',
    'app': 'C:\\Users\\dsb67\\Downloads\\instagram-291-1-0-34-111.apk',
    'noReset': True,
    'autoGrantPermissions': True,
    'appPackage': 'com.instagram.android',
    'appActivity': 'com.instagram.mainactivity.MainActivity'
    # Replace '/path/to/Instagram.apk' with the actual path to the Instagram APK file

}
appium_url = 'http://localhost:4723/wd/hub'

# Replace '4723' with the appropriate Appium server port

driver = webdriver.Remote(appium_url, desired_caps)
  # Wait for 30 seconds for the app to install


driver.quit()