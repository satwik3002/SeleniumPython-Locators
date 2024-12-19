from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up WebDriver
driver = webdriver.Chrome()  # Ensure ChromeDriver is in PATH

# Step 1: Launch the URL
driver.get("https://www.easycalculation.com/")
driver.maximize_window()
time.sleep(2)  # Wait for the page to load

# Step 2: Click on the "Love Calculator" link from the homepage
love_calculator_link = driver.find_element(By.LINK_TEXT, "Love Calculator")  # Find the link by text
love_calculator_link.click()
time.sleep(2)  # Wait for the Love Calculator page to load

# Step 3: Find all the links on the Love Calculator page
all_links = driver.find_elements(By.XPATH, ".//a")
print(f"Total number of links on the Love Calculator page: {len(all_links)}")

# Step 4: Close the browser
driver.quit()
