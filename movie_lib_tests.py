import unittest
from datetime import datetime
from movie_lib import Movie, User, Rating


movies ={1: Movie(1, 'Toy Story (1995)', datetime.strptime('01-Jan-1995', '%d-%b-%Y')),
        2: Movie(2, 'GoldenEye (1995)', datetime.strptime('01-Jan-1995', '%d-%b-%Y')),
        3: Movie(3, 'Four Rooms (1995)', datetime.strptime('01-Jan-1995', '%d-%b-%Y'))}

users = {308: User(308, 1, 4), 287: User(287, 1, 5),
        5: User(5, 2, 3), 268: User(268, 2, 2),
        181: User(181, 3, 2), 81: User(81, 3, 4)}


for movie_id, movie in movies.items():
    for user_id, user in users.items():
        if movie_id in user.ratings:
            movies[movie_id].add_rating(movie_id, user_id, user.ratings[movie_id])

# for movie_id, movie in movies.items():
#     print("Movie Name: ", movie.movie_title, "Release Date: ", movie.release_date, "Movie Ratings: ", movie.ratings)
ratings = Rating(movies, users)

class TestRating(unittest.TestCase):

    def test_assert_equal_average_rating(self):
        self.assertEqual(ratings.average_rating(movie_id=1), 4.5)

    def test_assert_equal_user_ratings(self):
        self.assertEqual(ratings.users_ratings(user_id=81), {3: 4})






if __name__ == '__main__':
    unittest.main()
