from django.urls import path
from library import views

app_name = 'library'

urlpatterns = [
    path('lists/', views.MovieListListView.as_view(), name='movielist_list'),
    path('lists/add/', views.MovieListCreateView.as_view(), name='movielist_create'),
    path('lists/<slug:slug>/', views.MovieListDetailView.as_view(), name='movielist_detail'),
    path('lists/<slug:slug>/edit/', views.MovieListUpdateView.as_view(), name='movielist_update'),
    path('lists/<slug:slug>/delete/', views.MovieListDeleteView.as_view(), name='movielist_delete'),
    
    path('plans/', views.WatchPlanListView.as_view(), name='watchplan_list'),
    path('plans/add/', views.WatchPlanCreateView.as_view(), name='watchplan_create'),
    path('plans/<slug:slug>/', views.WatchPlanDetailView.as_view(), name='watchplan_detail'),
    path('plans/<slug:slug>/edit/', views.WatchPlanUpdateView.as_view(), name='watchplan_update'),
    path('plans/<slug:slug>/delete/', views.WatchPlanDeleteView.as_view(), name='watchplan_delete'),
]
