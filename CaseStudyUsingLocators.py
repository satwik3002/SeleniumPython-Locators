from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Step 1: Launch the Easy Calculation website in Chrome
driver = webdriver.Chrome()  # Ensure ChromeDriver is in PATH or provide its full path
driver.get("https://www.easycalculation.com/")
driver.maximize_window()
time.sleep(2)

# Step 2: Click the "Sign In" button
sign_in_button = driver.find_element(By.XPATH, '//*[@id="wrap"]/div[2]/div[2]/span[2]/a/span')  # XPath for the "Sign In" button
sign_in_button.click()
time.sleep(3)

# Step 3: Enter Email/Username and Password, then click the login button
email_box = driver.find_element(By.ID, "log_email")  # ID locator for the email input field
email_box.send_keys("satwikkatamaraju@gmail.com")  # Replace with your email
time.sleep(1)

password_box = driver.find_element(By.NAME, "log_password")  # NAME locator for the password input field
password_box.send_keys("y5bq@YZZ5zDzUs")  # Replace with your password
time.sleep(1)

login_button = driver.find_element(By.XPATH, '//*[@id="log_frm"]/div[4]/input[1]')  # XPath locator for login button
login_button.click()
time.sleep(3)

# Step 4: After logging in, search for "Bangalore" in the search box and press Enter
search_box = driver.find_element(By.ID, "googleSearchId")  # NAME locator for the search box
search_box.send_keys("Bangalore")  # Type 'Bangalore' in the search box
search_box.send_keys(Keys.RETURN)  # Hit Enter to perform the search
time.sleep(3)



# Step 6: Close the browser
driver.quit()
print("Browser closed successfully.")


#//*[@id="wrap"]/div[2]/div[2]/span[2]/a/span
#//*[@id="log_frm"]/div[4]/input[1]