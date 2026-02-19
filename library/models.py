from django.db import models
from common.models import TimeStampMixin, SlugMixin


class MovieList(TimeStampMixin, SlugMixin, models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    movies = models.ManyToManyField('movies.Movie', related_name='lists')

    def __str__(self):
        return self.title

class WatchPlan(TimeStampMixin, SlugMixin, models.Model):
    AVERAGE_MOVIE_LENGTH = 120  # minutes

    title = models.CharField(max_length=50)
    movie_list = models.ForeignKey('library.MovieList', on_delete=models.CASCADE, related_name='watch_plans')
    planned_date = models.DateField()
    duration_hours = models.PositiveIntegerField()
    notes = models.TextField(blank=True)

    def estimated_total_minutes(self):
        movie_count = self.movie_list.movies.count()
        return movie_count * self.AVERAGE_MOVIE_LENGTH

    def estimated_total_hours(self):
        minutes = self.estimated_total_minutes()
        return round(minutes / 60, 1)

    def exceeds_available_time(self):
        available_minutes = self.duration_hours * 60
        return self.estimated_total_minutes() > available_minutes

    def __str__(self):
        return self.title
