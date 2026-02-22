from django.core.validators import MinValueValidator
from django.db import models
from django.templatetags.static import static
from django.utils.functional import cached_property
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

    @cached_property
    def cover_or_placeholder(self):
        if self.cover:
            return self.cover.url
        return static('images/no-image-placeholder.svg')

    def __str__(self):
        return self.title
