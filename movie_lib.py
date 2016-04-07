class Movie:
    def __init__(self, movie_id, movie_title, release_date):
        self.movie_id = movie_id
        self.movie_title = movie_title
        self. release_date = release_date

class User:
    def __init__(self, user_id, movie_id, rating):
        self.user_id = user_id
        self.movie_id = movie_id
        self.rating = rating


class Rating:
    def __init__(self, user_id=0, movie_id=0, rating=0):
        self.user_id = user_id
        self.movie_id = movie_id
        self. rating = rating
