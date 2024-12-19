import time
from selenium import webdriver
from selenium.webdriver.common.by import By


# Function to automate the test case
def automate_test(browser_name):
    # Initialize WebDriver
    if browser_name.lower() == "chrome":
        driver = webdriver.Chrome()
    elif browser_name.lower() == "edge":
        driver = webdriver.Edge()
    else:
        print("Unsupported browser.")
        return

    try:
        # Open the URL
        driver.get("https://www.easycalculation.com/index.php")
        driver.maximize_window()
        time.sleep(5)  # Allow page to load fully

        # Click on "Age Calculator" link
        driver.find_element(By.LINK_TEXT, "Age Calculator").click()
        time.sleep(5)  # Allow Age Calculator page to load

        # Count links and images on the page
        links = driver.find_elements(By.TAG_NAME, "a")
        images = driver.find_elements(By.TAG_NAME, "img")
        print(f"Total Links Found: {len(links)}")
        print(f"Total Images Found: {len(images)}")

        print("First 10 Links:")
        for link in links[:10]:
            print(link.get_attribute("href"))

        print("First 5 Images:")
        for img in images[:5]:
            print(img.get_attribute("src"))

        # Enter Date of Birth
        driver.find_element(By.ID, "i21").send_keys("03")  # Date
        driver.find_element(By.ID, "i22").send_keys("06")  # Month
        driver.find_element(By.ID, "i23").send_keys("2003")  # Year
        time.sleep(2)  # Pause to ensure inputs are processed

        # Click "GO" Button
        driver.find_element(By.XPATH, "//input[@name='but']").click()
        time.sleep(5)  # Wait for results to load

        # Print the result values
        print("Your Age is:", driver.find_element(By.XPATH, "//input[@id='r1']").get_attribute("value"))
        print("Your Age in Days:", driver.find_element(By.NAME, "val1").get_attribute("value"))
        print("Your Age in Hours:", driver.find_element(By.NAME, "val2").get_attribute("value"))
        print("Your Age in Minutes:", driver.find_element(By.NAME, "val3").get_attribute("value"))

        # Click "Reset"
        driver.find_element(By.XPATH, "//input[@onclick='clearall()']").click()
        time.sleep(2)  # Pause for reset action to complete

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the browser
        driver.quit()


# Test using Chrome browser
automate_test("chrome")
