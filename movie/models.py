from django.db import models


class Genre(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название жанра")

    def __str__(self):
        return self.title


class Movie(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название")
    release_year = models.PositiveIntegerField(verbose_name="Год выхода")
    genres = models.ManyToManyField(Genre, verbose_name="Жанры", null=True, blank=True)
    STARS_CHOICES = [
        ('⭐', '⭐'),
        ('⭐⭐', '⭐⭐'),
        ('⭐⭐⭐', '⭐⭐⭐'),
        ('⭐⭐⭐⭐', '⭐⭐⭐⭐'),
        ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐'),
    ]

    stars_rating = models.CharField("Популярность", max_length=10, choices=STARS_CHOICES)

    def __str__(self):
        return self.title
