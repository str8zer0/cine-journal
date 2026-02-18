from django.contrib import admin
from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'movie', 'rating', 'created_at')
    list_filter = ('rating', 'movie')
    search_fields = ('title', 'content', 'movie__title')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'modified_at', 'slug')
