from django.contrib import admin
from .models import MovieList, WatchPlan


@admin.register(MovieList)
class MovieListAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'description')
    filter_horizontal = ('movies',)
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'modified_at', 'slug')


@admin.register(WatchPlan)
class WatchPlanAdmin(admin.ModelAdmin):
    list_display = ('title', 'planned_date', 'duration_hours', 'movie_list')
    list_filter = ('planned_date',)
    search_fields = ('title', 'notes', 'movie_list__title')
    ordering = ('planned_date',)
    readonly_fields = ('created_at', 'modified_at', 'slug')
