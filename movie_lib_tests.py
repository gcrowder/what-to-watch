import unittest
import datetime
from movie_lib import Movie, User, Rating


movies =
        {1: Movie(1, 'Toy Story (1995)', datetime.strptime('01-Jan-1995')),
        2: Movie(2, 'GoldenEye (1995)', datetime.strptime('01-Jan-1995')),
        3: Movie(3, 'Four Rooms (1995)', datetime.strptime('01-Jan-1995'))}

users =
        {}






# class TestRating(unittest.TestCase):
#
#     def test_assert_true_get_rating(self):
#         test_rating = Rating(movie_id=1, rating=4, user_id=308)
#         self.assertTrue(test_rating.get_rating(308) == 4)
#







if __name__ == '__main__':
    unittest.main()
