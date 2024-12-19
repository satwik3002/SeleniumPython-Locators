import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up WebDriver
driver = webdriver.Chrome()  # Ensure ChromeDriver is in PATH

# Step 1: Launch the Easy Calculation website
driver.get("https://www.hollandandbarrett.com/shop/vitamins-supplements/vitamins/")
driver.maximize_window()
time.sleep(5)  # Wait for the page to load

ts1 = driver.find_element(By.TAG_NAME, "img").get_attribute("src")
print(len(ts1))

links = driver.find_elements(By.TAG_NAME, "a")
for link in links:
    print(link.text)
    print(link.get_attribute("herf"))