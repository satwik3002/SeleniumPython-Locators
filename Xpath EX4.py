from selenium import webdriver
from selenium.webdriver.common.keys import Keys  # Corrected import
from selenium.webdriver.common.by import By
import time

# Initialize WebDriver
driver = webdriver.Chrome()

# Open the automationpractice login page
driver.get("http://www.automationpractice.pl/index.php?controller=authentication&back=my-account")

# Maximize the browser window
driver.maximize_window()
time.sleep(5)

# Enter email
email_box = driver.find_element(By.ID, "email")
email_box.send_keys("satwikkatamaraju@gmail.com")
time.sleep(2)

# Enter password
password_box = driver.find_element(By.NAME, "passwd")
password_box.send_keys("@AAZGmkSB4CW@fq")
time.sleep(2)

# Click the login button
login_button = driver.find_element(By.XPATH, '//*[@id="SubmitLogin"]/span')
login_button.click()
time.sleep(5)