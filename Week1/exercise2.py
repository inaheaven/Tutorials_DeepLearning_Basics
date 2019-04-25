import urllib.request
from bs4 import BeautifulSoup
import pandas as pd

# In terminal, /Applications/Python\ 3.6/Install\ Certificates.command to issue ssl certs

url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn'
html = urllib.request.urlopen(url)
soup = BeautifulSoup(html, 'html.parser')

tags = soup.findAll('div', attrs={'class':'tit3'})

# print('-'*30)
# print(tags)
# print(len(tags))

# for tag in tags:
#     print(tag.a.string)

url_header = 'https://movie.naver.com'
# for tag in tags:
#     print(url_header + tag.a['href'])

url2 = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=cur&date=20180706'
html = urllib.request.urlopen(url2)
soup = BeautifulSoup(html, 'html.parser')

tit5 = soup.findAll('div', attrs={'class': 'tit5'})

# print('-'*50)
# print(tit5)
movie_title = []
for title in tit5:
    # print(title.a.string)
    num = len(title)
    movie_title.extend(title.a.string for n in range(0, num))

print(movie_title)
print(len(movie_title))
movie_points = []
points = soup.findAll('td', attrs={'class':'point'})
for point in points:
    # print(point.string)
    num = len(point)
    movie_points.extend(point.string for n in range(0, num))

print(movie_points)
print(len(movie_points))
# rates = pd.DataFrame({'title': movie_title, 'point': movie_points})
