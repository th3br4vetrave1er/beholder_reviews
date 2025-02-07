from dotenv import load_dotenv
import requests
import os
load_dotenv(dotenv_path='.env')

API_KEY = os.getenv('MOVIE_API_KEY')
BASE_URL = 'https://api.themoviedb.org/3/search/movie'

running = True

while running:
    def search_movie(movie_name):
        params = {
            'api_key': API_KEY,
            'query': movie_name
        }

        response = requests.get(BASE_URL, params=params)
        return response.json()

    movie_name = input('What movie should BEHOLDER search for?(x for exit)\n').lower()
    if movie_name == 'x':
        break
    data = search_movie(movie_name)

    def print_movie_info(data):
        if not data['results']:
            print('No such movie! Try again, mortal!')
            return

        movie = data['results'][0]
        title = movie['title']
        year = movie['release_date'][:4]
        rating = movie['vote_average']
        overview = movie['overview']
        poster_url = f'https://image.tmdb.org/t/p/w500{movie["poster_path"]}'

        print(f'🎬 Title: {title}')
        print(f'📅 Year: {year}')
        print(f'⭐ IMDb: {rating}')
        print(f'📝 About: {overview}')
        print(f'🎞️ Poster: {poster_url}')

    print_movie_info(data)