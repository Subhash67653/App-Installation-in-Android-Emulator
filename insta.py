import yaml
from appium import webdriver
from time import sleep
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy
import logging
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

with open('config.yml', 'r') as config_file:
    config = yaml.safe_load(config_file)

logging.info("Creating Appium driver")
logging.info("Appium desired capabilities: %s", config['login_capabilities'])
logging.info("Appium server URL: %s", config['url']['appium'])

try:
    driver = webdriver.Remote(config['url']['appium'], config['login_capabilities'])
    logging.info("Appium driver created: %s", driver)
    sleep(15)

    el8 = driver.find_element(by=AppiumBy.XPATH, value= "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText" )
    el8.send_keys("yourusername")

    el9 = driver.find_element(by=AppiumBy.XPATH, value= "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText" )
    el9.send_keys("password")

# Perform login action
    el13 = driver.find_element(by=AppiumBy.XPATH, value= "//android.view.View[@content-desc=\"Log in\"]")
    el13.click()

# Wait for the login process to complete
    sleep(5)

# Quit the driver and close the session
except WebDriverException as e:
    if "appPackage" in str(e):
        print("App is not installed")
    else:
        print("WebDriverException occurred:", str(e))

except NoSuchElementException as e:
    print("Element not found:", str(e))
    
except TimeoutException as e:
    print("Timeout occurred:", str(e))
    

    
except Exception as e:
    print("An error occurred:", str(e))

finally:
    # Quit the driver and close the session
    if 'driver' in locals():
        driver.quit()
        logging.info("Appium driver closed")








