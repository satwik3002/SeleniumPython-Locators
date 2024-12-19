from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select  # Import Select class
import time

# Set up WebDriver
driver = webdriver.Chrome()  # Ensure ChromeDriver is in PATH

# Step 1: Launch the target webpage
driver.get("http://www.automationpractice.pl/index.php?id_category=3&controller=category")
driver.maximize_window()
time.sleep(5)  # Wait for the page to load

# Step 2: Locate the dropdown element by its ID
dropdown = driver.find_element(By.ID, 'selectProductSort')  # Replace with the  ID of the dropdown
select = Select(dropdown)

# Step 3: Count the number of options
num_options = len(select.options)
print(f"There are {num_options} options in the dropdown list.")

# Step 4: Print all options in the dropdown
print("Dropdown options:")
for option in select.options:
    print(option.text)

# Clean up: Close the browser
driver.quit()
