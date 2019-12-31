import requests
from bs4 import BeautifulSoup


r = requests.get('https://www.nasdaq.com/')
c = r.content
# Create a soup object
soup = BeautifulSoup(c, 'lxml')