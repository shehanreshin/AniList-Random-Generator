import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Set the driver path and options
options = Options()
options.add_argument("--headless")  # Run in headless mode
options.add_argument("--no-sandbox")  # Bypass OS security model
options.add_argument("--disable-dev-shm-usage")  # Disable /dev/shm usage

driver = webdriver.Chrome(options=options)

# Get the URL of the page
url = "https://anilist.co/user/polkura/mangalist/Planning"

# Open the page
driver.get(url)

# Get the scroll height of the page
scroll_height = driver.execute_script("return document.body.scrollHeight")

# Scroll down to the bottom of the page 34 times
for _ in range(34):
    # Scroll down by the scroll height of the page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    # Wait for the page to load
    time.sleep(1)

    # Get the new scroll height of the page
    new_scroll_height = driver.execute_script("return document.body.scrollHeight")

    # If the new scroll height is the same as the old scroll height, then we have reached the bottom of the page
    if new_scroll_height == scroll_height:
        break

    # Update the scroll height
    scroll_height = new_scroll_height

# Get the page source
page_source = driver.page_source
print(page_source)

# Close the driver
driver.quit()
