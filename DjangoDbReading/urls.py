from django.urls import path

from movie.views import *

urlpatterns = [
    path('genre/add', AddGenreView.as_view(), name='add_genre'),
    path('movie/add', AddMovieView.as_view(), name="add_movie"),
    path('', GetMoviesView.as_view(), name="get_movies"),
    path('movie/<int:pk>', GetMovieView.as_view(), name="get_movie"),
]
