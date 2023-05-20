from bs4 import BeautifulSoup
import requests

year = "2000"
month = "01"
day = "01"

url = f"https://www.billboard.com/charts/hot-100/{year}-{month}-{day}/"
response = requests.get(url)
print("Response status code:", response.status_code) 

soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.select("li ul li h3")
song_names = []
for song_span in song_names_spans:
    song_name = song_span.getText().strip()
    song_names.append(song_name)

print(song_names)