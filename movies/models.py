from django.core.validators import MinValueValidator
from django.db import models
from common.models import TimeStampMixin, SlugMixin


class Genre(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name


class Movie(TimeStampMixin, SlugMixin, models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    release_year = models.PositiveIntegerField(validators=[MinValueValidator(1880)])
    cover = models.ImageField(upload_to='covers')
    imdb_link = models.URLField()
    watched = models.BooleanField(default=False)
    genres = models.ManyToManyField('Genre', related_name='movies_by_genre')
    tags = models.ManyToManyField('Tag', related_name='movies_by_tag', blank=True)

    def __str__(self):
        return self.title
