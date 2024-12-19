from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

# Initialize WebDriver
driver = webdriver.Chrome()

# Open the WebKul login page
driver.get("https://store.webkul.com/customer/account/login/")

# Maximize the browser window
driver.maximize_window()
time.sleep(5)

edit_box = driver.find_element(By.ID, "email")
edit_box.send_keys("satwikkatamaraju@gmail.com")
edit_box.send_keys(Keys.RETURN)
time.sleep(5)

edit_box = driver.find_element(By.NAME, "login[password]")
edit_box.send_keys("nGC?98Wt.h")
edit_box.send_keys(Keys.RETURN)
