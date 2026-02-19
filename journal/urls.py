from django.urls import path
from journal import views

app_name = 'journal'

urlpatterns = [
    path('', views.ReviewListView.as_view(), name='review_list'),
    path('add/<slug:movie_slug>/', views.ReviewCreateView.as_view(), name='review_create'),
    path('<slug:slug>/', views.ReviewDetailView.as_view(), name='review_detail'),
    path('<slug:slug>/edit/', views.ReviewUpdateView.as_view(), name='review_update'),
    path('<slug:slug>/delete/', views.ReviewDeleteView.as_view(), name='review_delete'),
]
