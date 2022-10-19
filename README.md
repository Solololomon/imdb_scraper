# IMDb-Scraper
This script will search IMDb's database for English films and tv series
that match the parameters entered by the user, returning (at most) 10 results.

This is done by using the 'requests' and 'bs4' (BeautifulSoup) packages to web-scrape
from IMDb's search function based on a URL that changes with the user's input.

It will return the Title, Year, Genre, Rating, Runtime, and Age Rating of each
film/tv series that matches the initial parameters.
