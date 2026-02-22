from PIL.ImageOps import cover
from django.core.management.base import BaseCommand
from django.template.context_processors import media
from django.utils.text import slugify
from datetime import date, timedelta
import random
from movies.models import Movie, Genre, Tag
from library.models import MovieList, WatchPlan
from journal.models import Review


LOREM = (
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
    "Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "
    "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi "
    "ut aliquip ex ea commodo consequat."
)

class Command(BaseCommand):
    help = "Seed the database with demo data for Cine Journal"


    def handle(self, *args, **kwargs):
        self.stdout.write("Clearing old data...")
        Review.objects.all().delete()
        WatchPlan.objects.all().delete()
        MovieList.objects.all().delete()
        Movie.objects.all().delete()
        Genre.objects.all().delete()
        Tag.objects.all().delete()

        self.stdout.write("Creating genres...")
        genre_names = [
            "Action", "Drama", "Comedy", "Sci-Fi", "Fantasy",
            "Thriller", "Horror", "Romance", "Adventure", "Mystery"
        ]
        genres = [Genre.objects.create(name=g) for g in genre_names]

        self.stdout.write("Creating tags...")
        tag_names = [
            "Classic", "New", "Popular", "Underrated", "Award-winning",
            "Family", "Dark", "Feel-good", "Epic", "Cult"
        ]
        tags = [Tag.objects.create(name=t) for t in tag_names]

        self.stdout.write("Creating movies...")
        movies = []
        for i in range(1, 16):
            title = f"Movie {i}"
            movie = Movie.objects.create(
                title=title,
                release_year=random.randint(1980, 2024),
                description=LOREM,
            )
            movie.genres.add(*random.sample(genres, k=random.randint(1, 3)))
            movie.tags.add(*random.sample(tags, k=random.randint(1, 3)))
            movies.append(movie)

        self.stdout.write("Creating movie lists...")
        lists = []
        for i in range(1, 16):
            title = f"List {i}"
            ml = MovieList.objects.create(
                title=title,
                description=LOREM
            )
            ml.movies.add(*random.sample(movies, k=random.randint(3, 7)))
            lists.append(ml)

        self.stdout.write("Creating watch plans...")
        for i in range(1, 16):
            WatchPlan.objects.create(
                title=f"Plan {i}",
                movie_list=random.choice(lists),  # must be a MovieList instance
                planned_date=date.today() + timedelta(days=random.randint(1, 60)),
                duration_hours=random.randint(1, 5),
                notes=LOREM
            )

        self.stdout.write("Creating reviews...")
        for i in range(1, 16):
            Review.objects.create(
                title=f"Review {i}",
                content=LOREM,
                rating=random.uniform(1.0, 10.0),
                movie=random.choice(movies),
            )

        self.stdout.write(self.style.SUCCESS("Database seeded successfully!"))