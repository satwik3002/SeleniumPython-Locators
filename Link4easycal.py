from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

# Initialize WebDriver
driver = webdriver.Chrome()

# Open the Hiox login page
driver.get("https://www.login.hiox.com/login?referrer=easycalculation.com")

# Maximize the browser window
driver.maximize_window()
time.sleep(5)

edit_box = driver.find_element(By.ID, "log_email")
edit_box.send_keys("satwikkatamaraju@gmail.com")
edit_box.send_keys(Keys.RETURN)
time.sleep(5)

edit_box = driver.find_element(By.NAME, "log_password")
edit_box.send_keys("y5bq@YZZ5zDzUs")
edit_box.send_keys(Keys.RETURN)
