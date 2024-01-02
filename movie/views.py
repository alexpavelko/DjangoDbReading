from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView

from .forms import GenreForm, MovieForm
from .models import Movie, Genre


class AddGenreView(CreateView):
    model = Genre
    form_class = GenreForm
    template_name = 'genre/add_genre.html'
    success_url = reverse_lazy('get_movies')


class AddMovieView(CreateView):
    model = Movie
    form_class = MovieForm
    template_name = 'movie/add_movie.html'
    success_url = reverse_lazy('get_movies')


class GetMoviesView(ListView):
    model = Movie
    template_name = 'movie/get_movies.html'
    context_object_name = 'movies'


class GetMovieView(DetailView):
    model = Movie
    template_name = 'movie/get_movie.html'
    context_object_name = 'movie'

