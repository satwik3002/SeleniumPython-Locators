import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up WebDriver
driver = webdriver.Chrome()  # Ensure ChromeDriver is in PATH

# Step 1: Launch the Easy Calculation website
driver.get("https://www.easycalculation.com/")
driver.maximize_window()
time.sleep(5)  # Wait for the page to load

# Step 2: Click the "Love Calculator" link using XPath Locator
love_calculator_link = driver.find_element(By.XPATH, '//*[@id="alarmContentDisplay"]/div[1]/div[6]/div[2]/div[1]/ul/li[2]/a')
love_calculator_link.click()  # Click the "Love Calculator" link
print("Navigated to the Love Calculator page.")
time.sleep(5)  # Wait for the Love Calculator page to load

# Step 3: Find all anchor links on the Love Calculator page
all_links = driver.find_elements(By.TAG_NAME, "a")

# Step 4: Check if any links are found
if len(all_links) > 0:
    print(f"Total number of links found on the Love Calculator page: {len(all_links)}")
    for link in all_links:
        # Print each link's text and href attribute
        print(f"Link Text: {link.text}, Href: {link.get_attribute('href')}")
else:
    print("No links found on the Love Calculator page.")

# Step 5: Close the browser
driver.quit()
