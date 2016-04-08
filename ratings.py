import csv
from datetime import datetime, date
from movie_lib import Movie, User, Rating


def format_time(date):
    try:
        return datetime.strptime(date, '%d-%b-%Y')
    except ValueError:
        return datetime(2000, 1, 1)

def get_movies():
    movies = {}
    with open('movies', encoding='latin_1') as f:
        reader = csv.DictReader(f, fieldnames=['movie_id', 'movie_title', 'date', 'something_else'], delimiter='|')
        for row in reader:
            #print("Movie ID: ", row['movie_id'], "Release Date: ", row['date'])
            movies.update({int(row['movie_id']) : Movie(int(row['movie_id']), row['movie_title'], format_time(row['date']))})
    return movies

def get_users():
    users = {}


def main():
    movies = get_movies()
    # for movie_id, movie in movies.items():
    #     print("Movie ID: ", movie.movie_id, "Movie Title: ", movie.movie_title)


if __name__ == '__main__':
    main()
