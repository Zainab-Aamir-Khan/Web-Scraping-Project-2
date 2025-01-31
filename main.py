from bs4 import BeautifulSoup
import requests

url = requests.get("https://news.ycombinator.com/news").text
soup = BeautifulSoup(url, 'lxml')

# print(requests.get("https://news.ycombinator.com/news").status_code)

main = soup.find('td', class_ = 'title')
print(main)



