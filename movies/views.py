from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Avg
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from common.mixins import FilteringMixin
from movies.forms import MovieForm, GenreForm, TagForm
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['genre_form'] = GenreForm()
        context['tag_form'] = TagForm()
        return context

    def get_success_url(self):
        return reverse_lazy('movies:detail', kwargs={'slug': self.object.slug})


class MovieUpdateView(SuccessMessageMixin, UpdateView):
    model = Movie
    form_class = MovieForm
    template_name = 'movies/movie_form.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    success_message = "Movie '%(title)s' was updated successfully."

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['genre_form'] = GenreForm()
        context['tag_form'] = TagForm()
        return context

    def get_success_url(self):
        return reverse_lazy('movies:detail', kwargs={'slug': self.object.slug})


class MovieDeleteView(DeleteView):
    model = Movie
    template_name = 'movies/movie_confirm_delete.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_success_url(self):
        messages.success(self.request, f"Movie '{self.object.title}' deleted successfully.")
        return reverse('movies:list')


class CategoriesManagementView(TemplateView):
    template_name = 'movies/categories.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['genres'] = Genre.objects.all()
        context['tags'] = Tag.objects.all()
        context['genre_form'] = GenreForm()
        context['tag_form'] = TagForm()
        return context


class GenreListView(ListView):
    model = Genre
    template_name = 'movies/genre_list.html'


class GenreCreateView(SuccessMessageMixin, CreateView):
    model = Genre
    form_class = GenreForm
    template_name = 'movies/genre_form.html'
    success_message = "Genre '%(name)s' was created successfully."

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse('movies:create')


class GenreUpdateView(SuccessMessageMixin, UpdateView):
    model = Genre
    form_class = GenreForm
    template_name = 'movies/genre_form.html'
    success_url = reverse_lazy('movies:categories')
    success_message = "Genre '%(name)s' was updated successfully."


class GenreDeleteView(DeleteView):
    model = Genre
    template_name = 'movies/genre_confirm_delete.html'

    def dispatch(self, request, *args, **kwargs):
        genre = self.get_object()
        if genre.movies_by_genre.exists():
            messages.error(request, f"You cannot delete genre '{genre.name}' because it is assigned to movies.")
            return redirect('movies:categories')
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        messages.success(self.request, f"Genre '{self.object.name}' deleted successfully.")
        return reverse('movies:categories')


class TagListView(ListView):
    model = Tag
    template_name = 'movies/tag_list.html'


class TagCreateView(SuccessMessageMixin, CreateView):
    model = Tag
    form_class = TagForm
    template_name = 'movies/tag_form.html'
    success_message = "Tag '%(name)s' was created successfully."

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse('movies:create')


class TagUpdateView(SuccessMessageMixin, UpdateView):
    model = Tag
    form_class = TagForm
    template_name = 'movies/tag_form.html'
    success_url = reverse_lazy('movies:categories')
    success_message = "Tag '%(name)s' was updated successfully."


class TagDeleteView(DeleteView):
    model = Tag
    template_name = 'movies/tag_confirm_delete.html'

    def dispatch(self, request, *args, **kwargs):
        tag = self.get_object()
        if tag.movies_by_tag.exists():
            messages.error(request, f"You cannot delete tag '{tag.name}' because it is assigned to movies.")
            return redirect('movies:categories')
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        messages.success(self.request, f"Tag '{self.object.name}' deleted successfully.")
        return reverse('movies:categories')
