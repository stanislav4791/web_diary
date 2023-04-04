import requests
from bs4 import BeautifulSoup

def ylenews_rss():
    article_list = []

    try:
        r = requests.get('https://feeds.yle.fi/uutiset/v1/majorHeadlines/YLE_UUTISET.rss')
        soup = BeautifulSoup(r.content, features='xml')
        
        articles = soup.findAll('item')

        for a in articles:
            title = a.find('title').text
            link = a.find('link').text
            description = a.find('description').text
            

            article = {
                'title': title,
                'link': link,
                'description': description
               }
            article_list.append(article)

        return article_list[0:5] 
        
    except Exception as e:
        print('newsscrape failed.')
        print(e)

ylenews_rss()

