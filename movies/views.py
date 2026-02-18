from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from movies.forms import MovieForm
from movies.models import Movie


class MovieListView(ListView):
    model = Movie
    template_name = 'movies/movie_list.html'
    context_object_name = 'movies'
    ordering = ['-created_at']


class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movies/movie_detail.html'
    context_object_name = 'movie'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'


class MovieCreateView(CreateView):
    model = Movie
    form_class = MovieForm
    fields = ['title', 'description', 'release_year', 'cover', 'imdb_link', 'watched', 'genres', 'tags']
    template_name = 'movies/movie_form.html'

    def get_success_url(self):
        return reverse_lazy('movie_detail', kwargs={'slug': self.object.slug})


class MovieUpdateView(UpdateView):
    model = Movie
    form_class = MovieForm
    fields = ['title', 'description', 'release_year', 'cover', 'imdb_link', 'watched', 'genres', 'tags']
    template_name = 'movies/movie_form.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_success_url(self):
        return reverse_lazy('movie_detail', kwargs={'slug': self.object.slug})


class MovieDeleteView(DeleteView):
    model = Movie
    template_name = 'movies/movie_confirm_delete.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    success_url = reverse_lazy('movie_list')
