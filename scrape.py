import requests
from bs4 import BeautifulSoup

response = requests.get('https://news.ycombinator.com/news')
soupobj = BeautifulSoup(response.text, 'html.parser')
# print(soupobj.find_all('div'))
# print(soupobj.find('a'))
# print(soupobj.select('.score'))
print(soupobj.select(''))