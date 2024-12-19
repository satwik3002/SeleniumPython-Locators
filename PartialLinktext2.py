import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up WebDriver
driver = webdriver.Chrome()  # Ensure ChromeDriver is in PATH

# Step 1: Launch the nopCommerce website
driver.get("https://www.nopcommerce.com/")  # URL of the nopCommerce website
driver.maximize_window()
time.sleep(5)  # Wait for the page to load

# Step 2: Find and click on a link using partial link text
partial_link = "nopCommerce"
link_element = driver.find_element(By.PARTIAL_LINK_TEXT, partial_link)
link_element.click()
time.sleep(5)  # Wait for the page to load

# Additional actions can be added as required, such as interacting with products or categories.
