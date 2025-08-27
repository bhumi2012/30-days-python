import requests
from bs4 import BeautifulSoup

# 1
# url = "https://quotes.toscrape.com/"
# response = requests.get(url)
# print("Status Code:", response.status_code) 
# soup = BeautifulSoup(response.text, "html.parser")
# print("Page Title:", soup.title.string)     
# quotes = soup.find_all("span", class_="text")
# print("Number of Quotes Found:", len(quotes))
# for q in quotes:
#     print(q.text)

# 2
# url = "https://webscraper.io/test-sites/e-commerce/static/computers/laptops"
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'html.parser')

# products = soup.find_all('div', class_='caption')

# for product in products:
#     name = product.find('a', class_='title').text.strip()
#     price = product.find('h4', class_='price').text.strip()
#     print(f"{name} → {price}")

# 3
url = "https://quotes.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

quotes = soup.find_all('span', class_='text')
authors = soup.find_all('small', class_='author')

for q, a in zip(quotes, authors):
    print(f"{q.text} — {a.text}")
