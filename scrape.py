import requests
from bs4 import BeautifulSoup

response = requests.get('https://news.ycombinator.com/news')
soupobj = BeautifulSoup(response.text, 'html.parser')
links = soupobj.select('.titleline')
votes = soupobj.select('.score')

print(links)



# print(soupobj.find_all('div'))
# print(soupobj.find('a'))
# print(soupobj.body.contents)
# print(soupobj.select('.score'))
# print(soupobj.select(''))