import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize WebDriver
driver = webdriver.Chrome()

# Open the Hiox login page
driver.get("https://www.login.hiox.com/login?referrer=easycalculation.com")

# Maximize the browser window
driver.maximize_window()
time.sleep(5)

# Input email address
email_box = driver.find_element(By.ID, "log_email")
email_box.send_keys("satwikkatamaraju@gmail.com")
time.sleep(2)

# Input password
password_box = driver.find_element(By.NAME, "log_password")
password_box.send_keys("y5bq@YZZ5zDzUs")
time.sleep(2)

# Click the login button
login_button = driver.find_element(By.XPATH, '//*[@id="log_frm"]/div[4]/input[1]')
login_button.click()
time.sleep(5)

# Close the browser
driver.quit()
