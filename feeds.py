"""
This is to get "The Brief" section from the time.com. API requested from any 
kind of python server is possible.
@author aarushibhatia
@licence MIT License
"""

from bs4 import BeautifulSoup
import requests


url = 'https://time.com/'
time_page = requests.get(url)

souped = BeautifulSoup(time_page.content, 'html5lib')
data_stream = souped.find_all(class_='column-tout-metadata')

def news_feed_json():
    """Returns top six feeds"""

    news_feed = []
    for data in range(3, 9):
        title = str(data_stream[data].get_text().strip())
        link = url + str(data_stream[data].a['href'])
        news_feed.append({"title":title, "link": link})

    return news_feed
