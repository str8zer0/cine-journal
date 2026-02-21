from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Avg
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from common.mixins import FilteringMixin
from movies.forms import MovieForm
from movies.models import Movie, Genre, Tag


class MovieListView(FilteringMixin, ListView):
    queryset = Movie.objects.annotate(avg_rating=Avg('reviews__rating'))
    template_name = 'movies/movie_list.html'
    context_object_name = 'movies'
    ordering = ['-created_at']
    paginate_by = 9

    filter_fields = {
        'title': 'title__icontains',
        'genre': 'genres__name__iexact',
        'tag': 'tags__name__iexact',
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_genres'] = Genre.objects.all().order_by('name')
        context['all_tags'] = Tag.objects.all().order_by('name')
        return context

class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movies/movie_detail.html'
    context_object_name = 'movie'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'


class MovieCreateView(SuccessMessageMixin, CreateView):
    model = Movie
    form_class = MovieForm
    template_name = 'movies/movie_form.html'
    success_message = "Movie '%(title)s' was created successfully."

    def get_success_url(self):
        return reverse_lazy('movies:detail', kwargs={'slug': self.object.slug})


class MovieUpdateView(SuccessMessageMixin, UpdateView):
    model = Movie
    form_class = MovieForm
    template_name = 'movies/movie_form.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    success_message = "Movie '%(title)s' was updated successfully."

    def get_success_url(self):
        return reverse_lazy('movies:detail', kwargs={'slug': self.object.slug})


class MovieDeleteView(DeleteView):
    model = Movie
    template_name = 'movies/movie_confirm_delete.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    success_url = reverse_lazy('movies:list')

    def post(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(request, f"Movie '{obj.title}' was deleted successfully.")
        return super().post(request, *args, **kwargs)
