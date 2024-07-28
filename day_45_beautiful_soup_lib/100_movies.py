from bs4 import BeautifulSoup
import requests


page_html = requests.get('https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/')
soup = BeautifulSoup(page_html.text, 'html.parser')

movies = soup.find_all(name='h3', attrs={'class': 'title'})

with open('movies.txt', 'w') as f:
    movie_titles = [movie.get_text() for movie in movies][::-1]
    f.write("\n".join(movie_titles))