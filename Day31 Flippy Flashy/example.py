from bs4 import BeautifulSoup
import requests

base_url = "https://secure.runescape.com/m=hiscore_oldschool_hardcore_ironman/overall?table=0&page={}"
users = []

# Scrape usernames from the first two pages
for page_num in range(1, 41):
    url = base_url.format(page_num)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    for row in soup.find_all('tr'):
        cells = row.find_all('td')
        for cell in cells:
            if "user1=" in str(cell):
                user = str(cell).split('user1=')[1].split('">')[0].replace('\xa0', ' ')
                user = user.replace('Ý', ' ')
                users.append(user)

print(users[:1000])
