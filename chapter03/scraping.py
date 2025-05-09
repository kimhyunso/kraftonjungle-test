import requests
import collections
collections.Callable = collections.abc.Callable

from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.imdb.com/chart/top/?ref_=nv_mv_250', headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')
# print(soup)  # HTML을 받아온 것을 확인

movies = soup.select('.cli-parent') # 클래스 cli-parent 를 선택
# print("--------------------------------")
# print(len(movies)) # 가져온 영화 개수
# print("--------------------------------")
# print(movies[0].select_one('h3').text)

# for movie in movies:
#     h3_element = movie.select_one('h3')
#     print(h3_element.text)


movie = movies[0]
elements = movie.select('span')
movie_name = movie.select_one('h3').text
movie_year = elements[0].text
movie_time = elements[1].text
movie_rating = elements[2].text

print(movie_name, movie_year, movie_time, movie_rating)


