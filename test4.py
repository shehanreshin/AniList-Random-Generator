from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

#options = Options()
#options.add_argument("--headless")  # Run in headless mode
#options.add_argument("--no-sandbox")  # Bypass OS security model
#options.add_argument("--disable-dev-shm-usage")  # Disable /dev/shm usage

driver = webdriver.Chrome()

url = "https://anilist.co/user/polkura/mangalist/Planning"  # Replace with the actual URL
driver.get(url)

scroll_pause_time = 1  # Pause duration between scrolls
scroll_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll to the bottom of the page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(scroll_pause_time)

    # Check if new content has been loaded
    new_scroll_height = driver.execute_script("return document.body.scrollHeight")
    if new_scroll_height == scroll_height:
        break

    scroll_height = new_scroll_height

page_source = driver.page_source

scraper = BeautifulSoup(page_source, "html.parser")
# Use BeautifulSoup methods to find and extract the desired content
driver.quit()

entry_rows = scraper.find_all('div', class_='entry row')
titles = []
progress_arr = []
formats = []

for row in entry_rows:
    
    title_div = row.find('div', class_='title')
    if title_div:
        title_content = title_div.text.strip()
        titles.append(title_content)

    progress_div = row.find('div', class_='progress')
    if progress_div:
        progress_content = progress_div.text.strip().replace('\n+','')
        if progress_content == "0":
            progress_content = "Ongoing"
        else:
            progress_content = "Complete"
        progress_arr.append(progress_content)

    format_div = row.find('div', class_='format')
    if format_div:
        format_content = format_div.text.strip()
        formats.append(format_content)

planned = []

for num in range(len(titles)):
    entry = {'title':titles[num], 'progress':progress_arr[num], 'format':formats[num]}
    planned.append(entry)

for entry in planned:
    if entry['title'] == 'Utsuro no Hako to Zero no Maria':
        print(entry)