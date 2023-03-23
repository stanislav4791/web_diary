import requests
from bs4 import BeautifulSoup
import json

def ylenews_rss():
    article_list = []

    try:
        r = requests.get('https://feeds.yle.fi/uutiset/v1/majorHeadlines/YLE_UUTISET.rss')
        soup = BeautifulSoup(r.content, features='xml')
        #return print(soup)
        articles = soup.findAll('item')

        for a in articles:
            title = a.find('title').text
            link = a.find('link').text
            #pubDate = a.find('pubDate').text
            description = a.find('description').text
            #enclosure = a.find('enclosure').url # how to scrape .jpg image

            article = {
                'title': title,
                'link': link,
                #'pubDate': pubDate,
                'description': description
                
                }
            article_list.append(article)

        #return print('newsscrape succeeded:', r.status_code)
        return article_list[0:5] 
        #print((article_list)[0:3])
        #print(('\n'.join(article_list)))
    except Exception as e:
        print('newsscrape failed.')
        print(e)

#def save_tolist(article_list):
 #   with open('articles2.txt', 'w') as f:
  #      for a in article_list:
   #         f.write(a)
    #    f.close()
        #json.dump(article_list, outfile)

#print('start newsscrape')
#print(ylenews_rss())
ylenews_rss()
#print('finished scraping')
