from bs4 import BeautifulSoup
import requests
from csv import writer

url = 'https://www.imdb.com/chart/top/'
page = requests.get(url, timeout=80)

soup = BeautifulSoup(page.content, 'lxml')
results = soup.find('tbody', class_='lister-list')
movies = results.find_all('tr')
with open('imdb.csv', 'w', newline='', encoding='utf8') as f:
    thewriter = writer(f)
    header = ['Position','Movie', 'Year', 'Rating', ' ']
    thewriter.writerow(header)
    counter = 1

    for result in movies:

        title_column = result.find('td', class_='titleColumn')

        title = title_column.find('a').text
        year = title_column.find('span', class_='secondaryInfo').text.replace('-', '')

        rating_column = result.find('td', class_='ratingColumn imdbRating')
        rating = rating_column.find('strong').text

        movieinfo = [counter ,title, year, rating]
        thewriter.writerow(movieinfo)
        counter+=1