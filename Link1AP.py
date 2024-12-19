from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

# Initialize WebDriver
driver = webdriver.Chrome()

# Open the automationpractice login page
driver.get("http://www.automationpractice.pl/index.php?controller=authentication&back=my-account")

# Maximize the browser window
driver.maximize_window()
time.sleep(5)

edit_box = driver.find_element(By.ID, "email")
edit_box.send_keys("satwikkatamaraju@gmail.com")
edit_box.send_keys(Keys.RETURN)
time.sleep(5)

edit_box = driver.find_element(By.NAME, "passwd")
edit_box.send_keys("@AAZGmkSB4CW@fq")
edit_box.send_keys(Keys.RETURN)
