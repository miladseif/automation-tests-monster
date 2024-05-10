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


# Navigate to the New Monster page
new_monster_link = driver.find_element(By.XPATH, "/html/body/app-root/div/div/div/app-monsters/div/div[1]/app-monster-list/div[1]/div[1]/button[1]")
new_monster_link.click()

# Fill in the new monster details
monster_name_input = driver.find_element(By.ID, "name")
monster_role_input = driver.find_element(By.XPATH, "/html/body/app-root/div/div/div/app-monsters/div/div[2]/app-monster-edit/div/div/form/div[4]/div/div/div/input[4]")
monster_description_input = driver.find_element(By.ID, "description")
favorite_checkbox = driver.find_element(By.ID, "favorite")

monster_name_input.send_keys("Phoenix")
monster_role_input.click()
monster_description_input.send_keys("Testing")

# Mark the monster as favorite
if not favorite_checkbox.is_selected():
    favorite_checkbox.click()

# Save the monster
save_button = driver.find_element(By.XPATH, "/html/body/app-root/div/div/div/app-monsters/div/div[2]/app-monster-edit/div/div/form/div[1]/div/button[1]")
save_button.click()


# Verify that the new monster was added to the monster list with the provided data
monster_list_items = driver.find_elements(By.XPATH, "/html/body/app-root/div/div/div/app-monsters/div/div[1]/app-monster-list/div[2]/div")
monster_added = False
for item in monster_list_items:
    if "Phoenix" in item.text and "Testing" in item.text:
        monster_added = True
        break

if monster_added:
    print("New monster added successfully!")
else:
    print("Failed to add new monster!")

# Close the browser
driver.quit()
