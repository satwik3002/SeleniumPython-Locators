from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize WebDriver
driver = webdriver.Chrome()

# Open the LetsKodeIt login page
driver.get("https://www.letskodeit.com/login")

# Maximize the browser window
driver.maximize_window()
time.sleep(5)

# Locate and interact with the email field
email_field = driver.find_element(By.ID, "email")
email_field.send_keys("satwikkatamaraju@gmail.com")  # Replace with your email
time.sleep(1)

# Locate and interact with the password field
password_field = driver.find_element(By.NAME, "password")
password_field.send_keys("wNGVn6@9xDytBDy")  # Replace with your password
time.sleep(1)

# Click the login button (assuming correct XPath)
login_button = driver.find_element(By.XPATH, '//button[text()="Login"]')  # Adjust based on the actual button text
login_button.click()
time.sleep(5)

# Close the browser
driver.quit()
