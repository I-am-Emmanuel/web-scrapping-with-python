import requests
from bs4 import BeautifulSoup

response = requests.get('https://news.ycombinator.com/news')
soupobj = BeautifulSoup(response.text, 'html.parser')
link = soupobj.select('.titleline')
vote = soupobj.select('.score')

def create_custome_hn(links, votes):
    hack_news = []
    for index, item in enumerate(links):
        title = links[index].getText()
        href = links[index].get('href', None)
        hack_news.append({'title': title, 'href': href})

    return hack_news


print(create_custome_hn(links=link, votes = vote))


# print(hack_news)



# print(soupobj.find_all('div'))
# print(soupobj.find('a'))
# print(soupobj.body.contents)
# print(soupobj.select('.score'))
# print(soupobj.select(''))