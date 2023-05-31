from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import random

options = Options()
options.add_argument("-headless")  # Run in headless mode
options.add_argument("--no-sandbox")  # Bypass OS security model
options.add_argument("--disable-dev-shm-usage")  # Disable /dev/shm usage
options.add_argument("--page-load-strategy=eager")

driver = webdriver.Chrome(options=options)

url = "https://anilist.co/user/polkura/mangalist/Planning"  # Replace with the actual URL

start_time = time.time()
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

end_time = time.time()  # Record the end time
execution_time = end_time - start_time  # Calculate the execution time

print(f"Scroll time: {execution_time} seconds")

start_time = time.time()

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

end_time = time.time()  # Record the end time
execution_time = end_time - start_time  # Calculate the execution time

print(f"Scrape time: {execution_time} seconds")

planned = []

for num in range(len(titles)):
    entry = {'title':titles[num], 'progress':progress_arr[num], 'format':formats[num]}
    planned.append(entry)

arr_length = len(planned)

random_numbers = []

for _ in range(10000):
    random_number = random.randint(0, arr_length)
    found = False
    for d in random_numbers:
        key = list(d.keys())[0]
        if random_number == key:
            d[random_number] += 1
            found = True
            break
    if not found:
        dict_entry = {random_number: 1}
        random_numbers.append(dict_entry)

max_key = list(max(random_numbers, key=lambda d: list(d.values())[0]).keys())[0]
#print(random_numbers)
#print(max_key)
print(planned[max_key])