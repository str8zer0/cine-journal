from django.db import models
from common.models import TimeStampMixin, SlugMixin


class MovieList(TimeStampMixin, SlugMixin, models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    movies = models.ManyToManyField('movies.Movie', related_name='lists')

    def __str__(self):
        return self.title

class WatchPlan(TimeStampMixin, SlugMixin, models.Model):
    title = models.CharField(max_length=50)
    movie_list = models.ForeignKey('library.MovieList', on_delete=models.CASCADE, related_name='watch_plans')
    planned_date = models.DateField()
    duration_hours = models.PositiveIntegerField()
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.title
