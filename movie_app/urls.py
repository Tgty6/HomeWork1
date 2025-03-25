from django.urls import path
from .views import director_list, director_detail, movie_list, movie_detail, review_list, review_detail

urlpatterns = [
    path('directors/', director_list),
    path('directors/<int:id>/', director_detail),
    path('movies/', movie_list),
    path('movies/<int:id>/', movie_detail),
    path('reviews/', review_list),
    path('reviews/<int:id>/', review_detail),
]
