import requests
from bs4 import BeautifulSoup
import pprint

page1 = requests.get('https://news.ycombinator.com/news')
page2 = requests.get('https://news.ycombinator.com/news?p=2')
soupobj1 = BeautifulSoup(page1.text, 'html.parser')
soupobj2 = BeautifulSoup(page2.text, 'html.parser')

link1 = soupobj1.select('.titleline')
# vote = soupobj.select('.score')
subtext1 = soupobj1.select('.subtext')
link2 = soupobj2.select('.titleline')
# vote = soupobj.select('.score')
subtext2 = soupobj2.select('.subtext')

mega_link = link1 + link2
mega_subtext = subtext1 + subtext2


def sorted_hack_news_list(hknlist:list) -> list:
    return sorted(hknlist, key=lambda k: k['votes'], reverse=True)

def create_custome_hackn(links, subtext):
    hack_news = []
    for index, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[index].select('.score')
        if len(vote):
            point = int(vote[0].getText().replace(' points', ''))
            if point > 99:
                hack_news.append({'title': title, 'href': href, 'votes': point})

    return sorted_hack_news_list(hknlist=hack_news)
 

pprint.pprint(create_custome_hackn(links=mega_link, subtext = mega_subtext))


# def create_custome_hn(links, votes):
#     hack_news = []
#     for index, item in enumerate(links):
#         points = int(votes[index].getText().replace(' points', ''))
#         if points > 99:
#             title = links[index].getText()
#             href = links[index].get('href', None)
#             hack_news.append({'title': title, 'href': href})

#     return hack_news
# pprint.pprint(create_custome_hn(links=link, votes = vote))


# print(hack_news)



# print(soupobj.find_all('div'))
# print(soupobj.find('a'))
# print(soupobj.body.contents)
# print(soupobj.select('.score'))
# print(soupobj.select(''))