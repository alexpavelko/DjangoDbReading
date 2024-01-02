from django.shortcuts import render, get_object_or_404, redirect

from .forms import GenreForm, MovieForm
from .models import Movie


def add_genre(request):
    if request.method == 'POST':
        form = GenreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_movies')
    else:
        form = GenreForm()
    return render(request, 'genre/add_genre.html', {'form': form})


def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_movies')
    else:
        print("-")
        form = MovieForm()
    return render(request, 'movie/add_movie.html', {'form': form})


def get_movies(request):
    movies = Movie.objects.all()
    return render(request, 'movie/get_movies.html', {'movies': movies})


def get_movie(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request, 'movie/get_movie.html', {'movie': movie})
