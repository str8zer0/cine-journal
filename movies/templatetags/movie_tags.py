from django.db.models import Avg
from django.template import Library
from movies.models import Movie


register = Library()

@register.simple_tag
def top_rated_movies(limit=3):
    return (
        Movie.objects
        .annotate(avg_rating=Avg('reviews__rating'))
        .order_by('-avg_rating')[:limit]
    )
