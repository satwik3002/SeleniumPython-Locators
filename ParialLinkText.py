import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up WebDriver
driver = webdriver.Chrome()  # Ensure ChromeDriver is in PATH

# Step 1: Launch the Easy Calculation website
driver.get("https://www.hollandandbarrett.com/")
driver.maximize_window()
time.sleep(5)  # Wait for the page to load

partial_link = "Vitamins"
link_element = driver.find_element(By.PARTIAL_LINK_TEXT, partial_link)
link_element.click()
time.sleep(5)