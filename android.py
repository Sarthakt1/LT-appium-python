from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
# Desired capabilities for Appium
desired_caps = {
    "deviceName": "Galaxy S22 Ultra 5G",
    "platformName": "Android",
    "platformVersion": "12",
    "app": "lt://APP10160351951731828750346119",  # Enter app_url here
    "isRealMobile": True,
    "build": "Flutter",
    "name": "Sample Test - Python",
    "network": False,
    "visual": True,
    "video": True
}


def startingTest():
    # Retrieve LambdaTest credentials from environment variables or hardcode them
    username = os.environ.get("LT_USERNAME", "sarthakt")  # Replace with your username
    accesskey = os.environ.get("LT_ACCESS_KEY", "sLBGRpVZ6NeHd8etRYHC8ajGZTzHORXJy7pL08q5XNxxp1okT0")  # Replace with your access key

    try:
        # Initialize Appium driver
        driver = webdriver.Remote(
            command_executor=f"https://{username}:{accesskey}@mobile-hub.lambdatest.com/wd/hub",
            desired_capabilities=desired_caps
        )

        # Execute the 'flutter:waitFor' script to wait for the element
        driver.execute_script("flutter:waitFor", [
            "eyJmaW5kZXJUeXBlIjoiQnlUZXh0IiwidGV4dCI6IkVtcGxveWVlIGNvdW50cnkifQ==", 
            20000  # Wait timeout in milliseconds
        ])

        # Wait until the element is clickable
        wait = WebDriverWait(driver, 20)  # Timeout in seconds
        employee_country = wait.until(
            EC.element_to_be_clickable((MobileBy.XPATH, "//*[@content-desc='Employee country']"))
        )

        # Click the element
        employee_country.click()

        # Quit the driver
        driver.quit()
    except Exception as e:
        print(f"An error occurred: {e}")
        driver.quit()


# Start the test
startingTest()
