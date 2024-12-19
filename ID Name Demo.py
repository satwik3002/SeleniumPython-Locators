from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize WebDriver
driver = webdriver.Chrome()

# Open the Holland & Barrett login page
driver.get("https://auth.hollandandbarrett.com/u/login")

# Maximize the browser window
driver.maximize_window()
time.sleep(5)

# Find the username field by its ID and enter the email
driver.find_element(By.ID, "username").send_keys("satwikkatamaraju@gmail.com")

# Find the password field by its NAME and enter the password
driver.find_element(By.NAME, "password").send_keys("Y2#ssv@Xp/xP8Wt")
driver.find_element(By.XPATH, '/html/body/main/section/div/div/div/form/div[2]/button').click()

time.sleep(5)



