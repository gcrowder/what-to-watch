class Movie:
    def __init__(self, movie_id, movie_title, release_date, user_id=0, rating=0):
        self.movie_id = movie_id
        self.movie_title = movie_title
        self.release_date = release_date
        self.ratings = {user_id : rating}

class User:
    def __init__(self, user_id, movie_id, rating):
        self.user_id = user_id
        self.ratings = {movie_id : rating}


class Rating:
    def __init__(self, movies, users):
        self.movies = movies #{movie_id : movie_object}
        self.users = users #{user_id : user object}

    def average_rating(movie_id):
        movie = self.movies[movie_id]
        return (sum(movie.ratings.values)) / len(movie.ratings)

    def users_ratings(user_id):
        user = self.users[user_id]
        return user.ratings

    def movies_ratings(movie_id):
        movie = self.movies[movie_id]
        return movie.ratings

    def get_movie_title(movie_id):
        movie = self.movies[movie_id]
        return movie.title
