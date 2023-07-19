from appium import webdriver
import logging
import yaml
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

with open('config.yml', 'r') as config_file:
    config = yaml.safe_load(config_file)

logging.info("Creating Appium driver")
logging.info("Appium desired capabilities: %s", config['install_capabilities'])
logging.info("Appium server URL: %s", config['url']['appium'])

try:
  driver = webdriver.Remote(config['url']['appium'], config['install_capabilities'])
  logging.info("Appium driver created: %s", driver)

except WebDriverException as e:
    print(f'An error occurred: {str(e)}')

finally:
    # Quit the driver and close the session
    if 'driver' in locals():
        driver.quit()
        logging.info("Appium driver closed")
