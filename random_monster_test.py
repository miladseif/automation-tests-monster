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


# Navigate to the Create Random Monster
create_random_monster_link = driver.find_element(By.XPATH, "/html/body/app-root/div/div/div/app-monsters/div/div[1]/app-monster-list/div[1]/div[1]/button[2]")
create_random_monster_link.click()


# Function to check if text "Number of monsters: 3" exists
def text_number_of_monsters_3_exists():
    try:
        text_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//p _ngcontent-c3[contains(text(), 'Number of monsters: 3')]")))
        return True
    except:
        return False

if text_number_of_monsters_3_exists:
    print("Create Random Monster added successfully!")
else:
    print("Failed to Create Random Monster!")

# Close the browser
driver.quit()
