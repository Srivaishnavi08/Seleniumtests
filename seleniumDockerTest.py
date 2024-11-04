from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

print("Test Execution Started")
options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')

# Start the Selenium WebDriver
driver = webdriver.Remote(
    command_executor='http://localhost:4444/wd/hub',
    options=options
)

# Maximize the window size
driver.maximize_window()
driver.get("http://host.docker.internal:8000")  # Access the local server
time.sleep(20)

try:
    # Wait for the "Get started free" link to be clickable
    link = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Get started free"))
    )
    link.click()  # Click the link
    time.sleep(10)  # Wait for any resulting page to load
except Exception as e:
    print(f"An error occurred while trying to click the link: {e}")


print("Test Execution Successfully Completed!")
