# What to Watch

##ratings.py
ratings.py has one positional argument: user_id. When called with the user_id, ratings.py will print out the top 20 overall films, the top 20 overall films unseen by the given user, and the top 20 (if there are 20) films recommended by the user's closest peers. The default value is 0, which will print the top 20 overall films and exit.

##movie_lib.py
This module implements the classes used by ratings.py. Each user is instantiated as a User object. Similarly, each movie is a Movie object. All users and movies are contained in one Rating object.

##movie_lib_tests.py
Short test suite to test the methods of movie_lib's classes.
