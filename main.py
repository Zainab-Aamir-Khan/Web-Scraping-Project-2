from bs4 import BeautifulSoup
import requests

url = requests.get("git push -u origin main").text
soup = BeautifulSoup(url, 'lxml')



