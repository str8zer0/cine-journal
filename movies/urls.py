from django.urls import path
from movies import views

app_name = 'movies'

urlpatterns = [
    path('', views.MovieListView.as_view(), name='list'),
    path('add/', views.MovieCreateView.as_view(), name='create'),
    path('<slug:slug>/', views.MovieDetailView.as_view(), name='detail'),
    path('<slug:slug>/edit/', views.MovieUpdateView.as_view(), name='update'),
    path('<slug:slug>/delete/', views.MovieDeleteView.as_view(), name='delete'),
]
