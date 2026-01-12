from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Launch the Browser (Firefox)
print("Launching Firefox...")
# This will try to auto-install geckodriver if missing
driver = webdriver.Firefox()

# Go to a Website
print("Opening Wikipedia...")
driver.get("https://www.wikipedia.org/")

#. Find the Search Box
# (Wikipedia uses the same ID 'search' for both browsers)
search_box = driver.find_element(By.NAME, "search")

#Type and Interact
search_term = "Python (programming language)"
print(f"Typing: {search_term}")

search_box.send_keys(search_term) # Type the text
time.sleep(1) # Pause for dramatic effect
search_box.send_keys(Keys.RETURN) # Press Enter key

# Keep it open
print("Search Complete! Press Enter in this terminal to close the browser...")
input() 

driver.quit()