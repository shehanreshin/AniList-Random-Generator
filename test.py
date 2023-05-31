from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

# Set up Chrome options to run in headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")

# Set up Chrome driver with the specified options
driver = webdriver.Chrome(options=chrome_options)

# Load the webpage
url = "https://anilist.co/user/polkura/mangalist/Planning"
driver.get(url)

# Wait for the page to load
time.sleep(2)

# Scroll to the bottom of the page until reaching the end
actions = ActionChains(driver)
prev_height = driver.execute_script("return document.body.scrollHeight")
while True:
    actions.send_keys(Keys.END).perform()
    time.sleep(1)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == prev_height:
        break
    prev_height = new_height

# Wait for the page to fully load
time.sleep(2)

# Get the page source after scrolling to the bottom
page_source = driver.page_source

# Close the browser
driver.quit()

# Now you can parse the page source or perform any further processing
# on the loaded webpage
print(page_source)
