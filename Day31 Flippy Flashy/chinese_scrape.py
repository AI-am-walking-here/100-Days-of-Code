import requests
from bs4 import BeautifulSoup
import pandas as pd

# Website of teh 1500 most common chinese characters.
url = 'https://learnchinesecharacters.academy/common-chinese-characters/'

# Spoof the website to bypass webscraping restrictions
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table containing the common Chinese characters
table = soup.find('table')

# Find the table headers (column names)
headers = []
for header in table.find_all('th'):
    headers.append(header.text.strip())

# Find the table rows and extract the data
rows = []
for row in table.find_all('tr')[1:]:
    data = {}
    for i, cell in enumerate(row.find_all('td')):
        data[headers[i]] = cell.text.strip()
    rows.append(data)

# Create a pandas DataFrame from the data
df = pd.DataFrame(rows)

# Save the DataFrame as a CSV file in the 'data' folder
df.to_csv('data/scraped_data.csv', index=False)