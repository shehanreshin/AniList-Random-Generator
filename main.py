import requests
from bs4 import BeautifulSoup

url = 'https://anilist.co/user/polkura/mangalist/Planning'
html = requests.get(url)

scraper = BeautifulSoup(html.content, 'html.parser')

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
    if entry['title'] == 'Adam to Eve':
        print(entry)