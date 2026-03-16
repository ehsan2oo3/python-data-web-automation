import requests
from bs4 import BeautifulSoup

url = "https://example.com"

try:
    response = requests.get(url, timeout=10, verify=False)
    soup = BeautifulSoup(response.text, "html.parser")

    paragraphs = soup.find_all("p")

    for p in paragraphs:
        print(p.text)

except Exception as e:
    print("Error:", e)