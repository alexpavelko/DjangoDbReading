from django.urls import path

from movie.views import *

urlpatterns = [
    path('genre/add', add_genre, name='add_genre'),
    path('movie/add', add_movie, name="add_movie"),
    path('movies', get_movies, name="get_movies"),
    path('', get_movies, name=""),
    path('movies/<int:movie_id>', get_movie, name="get_movie"),

]
