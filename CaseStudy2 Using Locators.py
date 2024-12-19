from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up WebDriver
driver = webdriver.Chrome()  # Ensure ChromeDriver is in PATH

try:
    # Step 1: Launch the URL
    driver.get("http://www.automationpractice.pl/index.php?controller=authentication&back=my-account")
    time.sleep(2)  # Wait for the page to load

    # Step 2: Click on the first sign-in button
    sign_in_button = driver.find_element(By.XPATH, '//*[@id="header"]/div[2]/div/div/nav/div[1]/a')
    sign_in_button.click()
    time.sleep(2)

    # Step 3: Enter Email Address and Password, then click the second sign-in button
    email_input = driver.find_element(By.ID, "email")
    password_input = driver.find_element(By.ID, "passwd")
    email_input.send_keys("satikkatamaraju@gmail.com")  # Replace with your email
    password_input.send_keys("@AAZGmkSB4CW@fq")        # Replace with your password

    second_sign_in_button = driver.find_element(By.ID, "SubmitLogin")
    second_sign_in_button.click()
    time.sleep(2)

    # Step 4: Click on DRESSES and then WOMEN
    dresses_tab = driver.find_element(By.XPATH, '//*[@id="block_top_menu"]/ul/li[2]/a')
    dresses_tab.click()
    time.sleep(2)
    women_tab = driver.find_element(By.XPATH, '//*[@id="block_top_menu"]/ul/li[1]/a')
    women_tab.click()
    time.sleep(2)

finally:
    # Step 5: Close the browser
    driver.quit()
