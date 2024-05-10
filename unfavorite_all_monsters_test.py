import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setting up the WebDriver (assuming Chrome WebDriver)
driver = webdriver.Chrome()

# Navigate to the website
driver.get("https://glitchitsystem.com/monster/")

# Login with provided credentials
username_input = driver.find_element(By.ID, "username")
password_input = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.XPATH, "/html/body/app-root/div/div/div/app-login/div/div/form/div[3]/div/button")

username_input.send_keys("bob@bob.com")
password_input.send_keys("Test123")

login_button.click()

# Wait for number of monsters text to load after successful login
number_of_monsters = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/app-root/div/div/div/app-monsters/div/div[1]/app-monster-list/p"))
)


# Click the "Unfavorite All" button
unfavorite_button = driver.find_element(By.XPATH, "/html/body/app-root/div/div/div/app-monsters/div/div[1]/app-monster-list/div[1]/div[2]/button[1]")
unfavorite_button.click()


    # Verify that the monster list heart icon removal
    time.sleep(2)  # Adding a short delay for the list to update

# Function to check if favorite icon exists
def favorite_icon_exists():
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "glyphicon-heart")))
        return True
    except:
        return False

    if favorite_icon_exists():
        print("All monsters unfavorited successfully!")
    else:
        print("Failed to unfavorited all monsters.")

# Close the browser
driver.quit()
