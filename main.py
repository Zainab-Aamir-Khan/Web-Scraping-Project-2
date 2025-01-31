from bs4 import BeautifulSoup
import requests

url = requests.get("https://news.ycombinator.com/news").text
soup = BeautifulSoup(url, 'lxml')

# print(requests.get("https://news.ycombinator.com/news").status_code)
mainContent = soup.find('table').text
# print(mainContent)

for main in soup.find_all('tr', class_ = 'athing submission'):

    print(main)



