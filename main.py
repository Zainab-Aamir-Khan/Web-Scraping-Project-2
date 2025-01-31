from bs4 import BeautifulSoup
import requests

url = requests.get("https://news.ycombinator.com/news").text
soup = BeautifulSoup(url, 'lxml')

# print(requests.get("https://news.ycombinator.com/news").status_code)
mainContent = soup.find('table').text
print(mainContent)

main = soup.find('tr', class_ = 'athing submission').text
print(main)



