import requests
import collections
collections.Callable = collections.abc.Callable
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.jungle

def parse_data():
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get('https://www.imdb.com/chart/top/?ref_=nv_mv_250', headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')
    movies = soup.select('.cli-parent')
    print(len(movies))

    for movie in movies:
        elements = movie.select('span')
        movie_name = movie.select_one('h3').text.split('. ')[1]
        movie_year = int(elements[0].text)
        time_split = list(map(int, elements[1].text.replace('h', '').replace('m', '').split(' ')))
        movie_time = time_split[0] * 60 + time_split[1]
        movie_rating = elements[2].text
        doc = {
            'name' : movie_name,
            'year' : movie_year,
            'time' : movie_time,
            'rating' : movie_rating
        }
        db.movies.insert_one(doc)


# if __name__ == '__main__':
#   parse_data()


# Q1. 영화 제목 ‘포레스트 검프'의 개봉 연도를 가져오기
forest = db.movies.find_one({'name': '포레스트 검프'})
print(forest['year'])

# Q2. '포레스트 검포'와 같은 년도에 개봉한 영화 제목들을 가져오기
movies = list(db.movies.find({'year': forest['year']}))
for movie in movies:
    print(movie['name'])

# Q3. '매트릭스 영화'의 개봉 연도를 1998년으로 만들기
db.movies.update_one({'name': '매트릭스'},{'$set':{'year':1998}})
print(db.movies.find_one({'name': '매트릭스'}))