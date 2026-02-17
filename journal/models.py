from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from common.models import TimeStampMixin, SlugMixin


class Review(TimeStampMixin, SlugMixin, models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    rating = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        validators=[
            MinValueValidator(1.0),
            MaxValueValidator(5.0)
        ]
    )
    movie = models.ForeignKey('movies.Movie', on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return f'{self.title} for {self.movie.title}'
