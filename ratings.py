import csv
import operator
from datetime import datetime
from movie_lib import Movie, User, Rating
import random


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
    with open ('data') as f:
        reader = csv.DictReader(f, fieldnames=['user_id', 'movie_id', 'rating', 'something_else'], delimiter='\t')
        for row in reader:
            user_id = int(row['user_id'])
            movie_id = int(row['movie_id'])
            rating = int(row['rating'])
            if user_id in users:
                users[user_id].add_rating(user_id, movie_id, rating)
            else:
                users.update({user_id: User(user_id, movie_id, rating)})
    return users

def make_movie_ratings(movies, users):
    for movie_id, movie in movies.items():
        for user_id, user in users.items():
            if movie_id in user.ratings:
                movies[movie_id].add_rating(movie_id, user_id, user.ratings[movie_id])
    return movies

def prepare_ratings():
    movies = get_movies()
    users = get_users()
    movies = make_movie_ratings(movies, users)
    all_ratings = Rating(movies, users)
    return all_ratings

def most_popular_movies(ratings_object):
    averaged_movie_ratings = []
    for movie_id in ratings_object.movies.keys():
        if len(ratings_object.movies[movie_id].ratings) > 9:
            averaged_movie_ratings.append((movie_id, ratings_object.average_rating(movie_id)))
    descending_averaged_movie_ratings = sorted(averaged_movie_ratings, key=operator.itemgetter(1), reverse=True)
    return descending_averaged_movie_ratings

def show_movies(ratings_object, top_movies):
    count = 0
    for movie_id, rating in top_movies:
        count += 1
        if count < 21:
            print("{}. {}: {}".format(count, ratings_object.movies[movie_id].movie_title, round(rating, 2)))

def top_rated_unseen_movies(ratings_object, user_id):
    averaged_movie_ratings = []
    for movie_id in ratings_object.movies.keys():
        if len(ratings_object.movies[movie_id].ratings) > 9:
            if user_id not in ratings_object.movies[movie_id].ratings:
                averaged_movie_ratings.append((movie_id, ratings_object.average_rating(movie_id)))
    descending_averaged_movie_ratings = sorted(averaged_movie_ratings, key=operator.itemgetter(1), reverse=True)
    return descending_averaged_movie_ratings

def main():
    movie_user_ratings = prepare_ratings()
    pop_movies = most_popular_movies(movie_user_ratings)
    user_id = random.randint(1,943)
    recommended_movies = top_rated_unseen_movies(movie_user_ratings, user_id)
    print("Top 20 Films Overall: ")
    show_movies(movie_user_ratings, pop_movies)
    print("Top 20 Films Recommended for User: {}".format(user_id))
    show_movies(movie_user_ratings, recommended_movies)




if __name__ == '__main__':
    main()
