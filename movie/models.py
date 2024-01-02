from django.db import models


class Genre(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название жанра")

    def __str__(self):
        return self.title


class Movie(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название")
    release_date = models.DateField(verbose_name="Дата выхода")
    genres = models.ManyToManyField(Genre, verbose_name="Жанры", null=True, blank=True)
    stars_rating = models.IntegerField(verbose_name="Популярность")

    def __str__(self):
        return self.title
