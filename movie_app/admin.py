from django.contrib import admin
from .models import Director, Movie, Review

@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'duration', 'director')
    search_fields = ('title',)
    list_filter = ('director',)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'movie', 'text')
    search_fields = ('movie__title', 'text')
