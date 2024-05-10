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


# Navigate to the Sort Monsters
Sort_Monsters_link = driver.find_element(By.XPATH, "/html/body/app-root/div/div/div/app-monsters/div/div[1]/app-monster-list/div[1]/div[2]/button[3]")
Sort_Monsters_link.click()

# Function to get the list of monster names
def get_monster_names():
    monster_elements = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "col-xs-12")))
    monster_names = [element.text for element in monster_elements]
    return monster_names

# Function to check if monster list is sorted by name
def is_monster_list_sorted_by_name(monster_names):
    sorted_monster_names = sorted(monster_names)
    return monster_names == sorted_monster_names

try:
    # Get the list of monster names
    monster_names = get_monster_names()

# Check if the monster list is sorted by name
    if is_monster_list_sorted_by_name(monster_names):
        print("Monster list is sorted by name - PASSED")
    else:
        print("Monster list is not sorted by name - FAILED")

# Close the browser
driver.quit()
