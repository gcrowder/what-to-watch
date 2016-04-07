import unittest
from movie_lib import Movie, User, Rating

test_rating = Rating(movie_id=1, rating=4, user_id=308)

class TestRating:

    def test_assert_equal_add_rating(self, rating, user_id, movie_id):
        self.assertEqual(test_rating.get_rating(308), 4)
