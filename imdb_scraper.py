import requests
from bs4 import BeautifulSoup
import re

print('Welcome to the IMDb Film/TV Series Web Scraper (Please fill in all the fields)')
print()

title = input('Title to search: ')

while True:
    try:
        startyear = int(input('Start year of your search: '))
    except ValueError:
        print('Please enter a number')
        continue
    if startyear <= 2022 and 1900 <= startyear:
        break
    else:
        print('Please enter a date between 1900 and 2022')

while True:
    try:
        endyear = int(input('End year of your search: '))
    except ValueError:
        print('Please enter a number')
        continue
    if endyear <= 2022 and 1900 <= endyear:
        if endyear >= startyear:
            break
        else:
            print('End year must not be before the start year')
            continue
    else:
        print('Please enter a date between 1900 and 2022')

while True:
    try:
        minrat = float(input('Minimum rating to consider: '))
    except ValueError:
        print('Please enter a number')
        continue
    if minrat <= 10.0 and 1.0 <= minrat:
        break
    else:
        print('Please enter a number between 1.0 and 10.0')

while True:
    try:
        maxrat = float(input('Maximum rating to consider: '))
    except ValueError:
        print('Please enter a number')
        continue
    if maxrat <= 10.0 and 1.0 <= maxrat:
        if maxrat >= minrat:
            break
        else:
            print('Maximum rating must not be lower than minimum rating')
            continue
    else:
        print('Please enter a number between 1.0 and 10.0')

while True:
    try:
        minvote = int(input('Minimum number of votes to consider: '))
    except ValueError:
        print('Please enter an integer')
        continue
    if minvote >= 0:
        break
    else:
        print('Please enter a positive integer')

URL = f'https://www.imdb.com/search/title/?title={title}&title_type=feature,tv_series&release_date={startyear}-01-01,{endyear}-12-31&user_rating={minrat},{maxrat}&num_votes={minvote},&languages=en'

page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(class_='lister-list')
film_elements = results.find_all(class_='lister-item-content')

for film_element in film_elements:
    title_element = film_element.find('a')
    print(f'Title: {title_element.text.strip()}')
    year_element = film_element.find(class_='lister-item-year text-muted unbold')
    print(f'Year: {year_element.text.strip()}')
    genre_element = film_element.find(class_='genre')
    print(f'Genre: {genre_element.text.strip()}')
    rating_element = film_element.find('strong')
    print(f'Rating: {rating_element.text.strip()}')
    runtime_element = film_element.find(class_='runtime')
    print(f'Runtime: {runtime_element.text.strip()}')
    try:
        age_element = film_element.find(class_='certificate')
        print(f'Age Rating: {age_element.text.strip()}')
        pass
    except AttributeError:
        print('Age Rating: N/a')
        pass
    print()


