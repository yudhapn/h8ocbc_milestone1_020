"""
This is the movie module and supports all the REST actions for the
movie data
"""

from flask import make_response, abort
from config import db
from models import Director, Movie, MovieSchema
from pprint import pprint

def read_all():
    """
    This function responds to a request for /api/director/movies
    with the complete list of movies, sorted by movie title

    :return:                json list of all movies for all director
    """
    
    # Query the database for all the movies
    movies = Movie.query.order_by(db.desc(Movie.title)).limit(8).all()
    # print('movie data director:', movies[0].director)
    pprint(vars(movies[0]))
    # Serialize the list of movies from our data
    movie_schema = MovieSchema(many=True)
    data = movie_schema.dump(movies)
    return data

def read_top_rated():
    """
    This function responds to a request for /api/movies/top_rated
    with the complete list of movies, sorted by movie title

    :return:                json list of all movies for all director
    """
    
    # Query the database for all the movies
    movies = Movie.query.order_by(db.desc(Movie.vote_average)).limit(8).all()
    # print('director data:')
    pprint(vars(movies[0]))
    # Serialize the list of movies from our data
    movie_schema = MovieSchema(many=True)
    data = movie_schema.dump(movies)
    return data

def read_popular():
    """
    This function responds to a request for /api/movies/popular
    with the complete list of movies, sorted by movie title

    :return:                json list of all movies for all director
    """
    
    # Query the database for all the movies
    movies = Movie.query.order_by(db.desc(Movie.popularity)).limit(8).all()
    # print('movie data director:', movies[0].director)
    pprint(vars(movies[0]))
    # Serialize the list of movies from our data
    movie_schema = MovieSchema(many=True)
    data = movie_schema.dump(movies)
    return data

def read_by_title(title):
    """
    This function responds to a request for /api/movies/{title}
    with the complete list of movies, sorted by movie title

    :return:                json list of all movies for all director
    """
    
    # Query the database for all the movies
    movies = (Movie.query.filter(
        Movie.title.like(f"%{title}%")).limit(8))
    # print('movie data director:', movies[0].director)
    pprint(vars(movies[0]))
    # Serialize the list of movies from our data
    movie_schema = MovieSchema(many=True)
    data = movie_schema.dump(movies)
    return data

def read_one(director_id, movie_id):
    """
    This function responds to a request for
    /api/director/{director_id}/movies/{movie_id}
    with one matching movie for the associated director

    :param director_id:       Id of director the movie is related to
    :param movie_id:         Id of the movie
    :return:                json string of movie contents
    """
    # Query the database for the movie
    movie = (
        Movie.query.join(Director, Director.id == Movie.director_id)
        .filter(Director.id == director_id)
        .filter(Movie.id == movie_id)
        .one_or_none()
    )

    # Was a movie found?
    if movie is not None:
        movie_schema = MovieSchema()
        data = movie_schema.dump(movie)
        return data

    # Otherwise, nope, didn't find that movie
    else:
        abort(404, f"Movie not found for Id: {movie_id}")


def create(director_id, movie):
    """
    This function creates a new movie related to the passed in director id.

    :param director_id:       Id of the director the movie is related to
    :param movie:            The JSON containing the movie data
    :return:                201 on success
    """
    # get the parent director
    director = Director.query.filter(Director.id == director_id).one_or_none()

    # Was a director found?
    if director is None:
        abort(404, f"Director not found for Id: {director_id}")

    # Create a movie schema instance
    schema = MovieSchema()
    new_movie = schema.load(movie, session=db.session)

    # Add the movie to the director and database
    director.movies.append(new_movie)
    db.session.commit()

    # Serialize and return the newly created movie in the response
    data = schema.dump(new_movie)

    return data, 201


def update(director_id, movie_id, movie):
    """
    This function updates an existing movie related to the passed in
    director id.

    :param director_id:       Id of the director the movie is related to
    :param movie_id:         Id of the movie to update
    :param content:            The JSON containing the movie data
    :return:                200 on success
    """
    update_movie = (
        Movie.query.filter(Director.id == director_id)
        .filter(Movie.id == movie_id)
        .one_or_none()
    )

    # Did we find an existing movie?
    if update_movie is not None:

        # turn the passed in movie into a db object
        schema = MovieSchema()
        update = schema.load(movie, session=db.session)

        # Set the id's to the movie we want to update
        update.director_id = update_movie.director_id
        update.id = update_movie.id

        # merge the new object into the old and commit it to the db
        db.session.merge(update)
        db.session.commit()

        # return updated movie in the response
        data = schema.dump(update_movie)

        return data, 200

    # Otherwise, nope, didn't find that movie
    else:
        abort(404, f"Movie not found for Id: {movie_id}")


def delete(director_id, movie_id):
    """
    This function deletes a movie from the movie structure

    :param director_id:   Id of the director the movie is related to
    :param movie_id:     Id of the movie to delete
    :return:            200 on successful delete, 404 if not found
    """
    # Get the movie requested
    movie = (
        Movie.query.filter(Director.id == director_id)
        .filter(Movie.id == movie_id)
        .one_or_none()
    )

    # did we find a movie?
    if movie is not None:
        db.session.delete(movie)
        db.session.commit()
        return make_response(
            "Movie {id} deleted".format(id=movie_id), 200
        )

    # Otherwise, nope, didn't find that movie
    else:
        abort(404, f"Movie not found for Id: {movie_id}")