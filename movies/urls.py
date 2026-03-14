from django.urls import path, include
from movies import views

app_name = 'movies'

genres_urlpatterns = [
    path('', views.GenreListView.as_view(), name='genre_list'),
    path('add/', views.GenreCreateView.as_view(), name='genre_create'),
    path('<int:pk>/edit/', views.GenreUpdateView.as_view(), name='genre_update'),
    path('<int:pk>/delete/', views.GenreDeleteView.as_view(), name='genre_delete'),
]

tags_urlpatterns = [
    path('', views.TagListView.as_view(), name='tag_list'),
    path('add/', views.TagCreateView.as_view(), name='tag_create'),
    path('<int:pk>/edit/', views.TagUpdateView.as_view(), name='tag_update'),
    path('<int:pk>/delete/', views.TagDeleteView.as_view(), name='tag_delete'),
]

urlpatterns = [
    path('', views.MovieListView.as_view(), name='list'),
    path('add/', views.MovieCreateView.as_view(), name='create'),
    path('categories/', views.CategoriesManagementView.as_view(), name='categories'),

    # GENRES AND TAGS
    path('genres/', include(genres_urlpatterns)),
    path('tags/', include(tags_urlpatterns)),

    # MOVIES (slug routes)
    path('<slug:slug>/', views.MovieDetailView.as_view(), name='detail'),
    path('<slug:slug>/edit/', views.MovieUpdateView.as_view(), name='update'),
    path('<slug:slug>/delete/', views.MovieDeleteView.as_view(), name='delete'),
]
