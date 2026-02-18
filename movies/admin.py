from django.contrib import admin
from movies.models import Genre, Tag, Movie


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_year', 'watched', 'created_at')
    list_filter = ('watched', 'release_year', 'genres', 'tags')
    search_fields = ('title', 'description')
    ordering = ('-created_at',)
    filter_horizontal = ('genres', 'tags')
    readonly_fields = ('created_at', 'modified_at', 'slug')
