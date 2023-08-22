import requests
from bs4 import BeautifulSoup
import pprint

response = requests.get('https://news.ycombinator.com/news')
soupobj = BeautifulSoup(response.text, 'html.parser')
link = soupobj.select('.titleline')
vote = soupobj.select('.score')
subtext = soupobject.select('.subtext')

# def create_custome_hn(links, votes):
#     hack_news = []
#     for index, item in enumerate(links):
#         points = int(votes[index].getText().replace(' points', ''))
#         if points > 99:
#             title = links[index].getText()
#             href = links[index].get('href', None)
#             hack_news.append({'title': title, 'href': href})

#     return hack_news

def create_custome_hackn(links, subtext):
    hack_news = []
    for index, item in enumerate(links):
        title = item[index].getText()
        href = item[index].get('href', None)
        vote = subtext[index].select('.score')
        if len(vote):
            point = int(vote[0].getText().replace(' points', ''))
            if point > 99:
                hack_news.append({'title': title, 'href': href, 'votes': point})

    return hack_news
 

pprint.pprint(create_custome_hn(links=link, votes = subtext))


# print(hack_news)



# print(soupobj.find_all('div'))
# print(soupobj.find('a'))
# print(soupobj.body.contents)
# print(soupobj.select('.score'))
# print(soupobj.select(''))