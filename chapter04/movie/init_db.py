import re
import random
import requests

from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.jungle

def insert_all():
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get('https://search.daum.net/search?w=tot&q=역대관객순위&DA=MOR&rtmaxcoll=MOR', headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')

    movies = soup.select('* c-list-doc > c-doc')

    for movie in movies:
        tag_element = movie.select_one('c-title')
        if not tag_element:
            continue
        title = tag_element.string.strip()
        info_url = f'https://search.daum.net/search{tag_element["data-href"]}'

        tag_element = movie.select_one('c-thumb')
        if not tag_element:
            continue

        poster_url = tag_element['data-original-src']
        tag_element = movie.select_one('c-contents-desc')
        if not tag_element:
            continue
        viewers = tag_element.string
        viewers = viewers.replace('만', '0,000')
        viewers = re.findall(r'[0-9]+', viewers)
        viewers = ''.join(viewers)
        viewers = int(viewers)

        tag_element = movie.select_one('c-contents-desc-sub')
        if not tag_element:
            continue
        open_date = tag_element.string.replace('.', ' ').strip().replace(' ', '.')
        (open_year, open_month, open_day) = [int(element) for element in open_date.split('.')]

        likes = random.randrange(0, 100)

        found = list(db.movies.find({'title': title}))
        if found:
            continue
        doc = {
            'title': title,
            'open_year': open_year,
            'open_month': open_month,
            'open_day': open_day,
            'viewers': viewers,
            'poster_url': poster_url,
            'info_url': info_url,
            'likes': likes,
            'trashed': False,
        }

        db.movies.insert_one(doc)
        print('완료: ', title, open_year, open_month, open_day, viewers, poster_url, info_url)


if __name__ == '__main__':
    db.movies.drop()
    insert_all()

