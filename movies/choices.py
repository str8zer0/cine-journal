from django.db import models


class GenreChoices(models.TextChoices):
    ACTION = 'action', 'Action'
    SCI_FI = 'sci-fi', 'Sci-Fi'
    DRAMA = 'drama', 'Drama'
    ANIMATION = 'animation', 'Animation'
    DOCUMENTARY = 'documentary', 'Documentary'
    FANTASY = 'fantasy', 'Fantasy'
    HORROR = 'horror', 'Horror'
    ROMANCE = 'romance', 'Romance'
    COMEDY = 'comedy', 'Comedy'
    THRILLER = 'thriller', 'Thriller'
    OTHER = 'other', 'Other'
