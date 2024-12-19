#MonthDropBox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select  # Import Select class
import time

# Set up WebDriver
driver = webdriver.Chrome()  # Ensure ChromeDriver is in PATH

# Step 1: Launch the URL
driver.get("https://www.facebook.com/campaign/landing.php")
driver.maximize_window()
time.sleep(5)  # Wait for the page to load

# Locate the dropdown and create a Select object
dropdown = driver.find_element(By.ID, 'month')  # Use find_element, not find_elements
select = Select(dropdown)

# Count the number of options in the dropdown
num_options = len(select.options)
print(f"There are {num_options} options in the month Dropdown")

# Print all options in the dropdown
for option in select.options:
    print(option.text)

# Clean up: Close the browser
driver.quit()

#YearDropBox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select  # Import Select class
import time

# Set up WebDriver
driver = webdriver.Chrome()  # Ensure ChromeDriver is in PATH

# Step 1: Launch the URL
driver.get("https://www.facebook.com/campaign/landing.php")
driver.maximize_window()
time.sleep(5)  # Wait for the page to load

# Locate the dropdown and create a Select object
dropdown = driver.find_element(By.ID, 'year')  # Use find_element, not find_elements
select = Select(dropdown)

# Count the number of options in the dropdown
num_options = len(select.options)
print(f"There are {num_options} options in the year Dropdown")

# Print all options in the dropdown
for option in select.options:
    print(option.text)

# Clean up: Close the browser
driver.quit()

#Day DropBox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select  # Import Select class
import time

# Set up WebDriver
driver = webdriver.Chrome()  # Ensure ChromeDriver is in PATH

# Step 1: Launch the URL
driver.get("https://www.facebook.com/campaign/landing.php")
driver.maximize_window()
time.sleep(5)  # Wait for the page to load

# Locate the dropdown and create a Select object
dropdown = driver.find_element(By.ID, 'day')  # Use find_element, not find_elements
select = Select(dropdown)

# Count the number of options in the dropdown
num_options = len(select.options)
print(f"There are {num_options} options in the day Dropdown")

# Print all options in the dropdown
for option in select.options:
    print(option.text)

# Clean up: Close the browser
driver.quit()
