import requests
from bs4 import BeautifulSoup
url = "https://www.bbc.com/news"
headers = {
"User-Agent": "Mozilla/5.0"
}
try:
response = requests.get(url, headers=headers, timeout=10)
response.raise_for_status()
soup = BeautifulSoup(response.text, "html.parser")
headlines = []
for tag in soup.find_all("h2"):
text = tag.get_text(strip=True)
if text:
headlines.append(text)
with open("headlines.txt", "w", encoding="utf-8") as file:
for headline in headlines:
file.write(headline + "\n")
print(f"Successfully saved {len(headlines)} headlines.")
except requests.RequestException as error:
print("Error while fetching the website:", error)
except Exception as error:
print("An unexpected error occurred:", error)
