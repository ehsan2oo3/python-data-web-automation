import requests
from bs4 import BeautifulSoup

url = "https://example.com"

response = requests.get(url, verify=False)

soup = BeautifulSoup(response.text, "html.parser")

paragraphs = soup.find_all("p")

for p in paragraphs:
    print(p.text)