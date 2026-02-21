from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from common.mixins import FilteringMixin
from journal.forms import ReviewForm
from journal.models import Review
from movies.models import Movie


class ReviewListView(FilteringMixin, ListView):
    queryset = Review.objects.select_related('movie')
    template_name = 'journal/review_list.html'
    context_object_name = 'reviews'
    ordering = ['-created_at']
    paginate_by = 10

    filter_fields = {
        'title': 'title__icontains',
        'movie': 'movie__title__icontains',
        'rating': 'rating__gte'
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ratings'] = range(1, 11)
        return context


class ReviewDetailView(DetailView):
    model = Review
    template_name = 'journal/review_detail.html'
    context_object_name = 'review'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'


class ReviewCreateView(SuccessMessageMixin, CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'journal/review_form.html'
    success_message = "Review '%(title)s' was created successfully."

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['movie'] = get_object_or_404(Movie, slug=self.kwargs['movie_slug'])
        return kwargs

    def form_valid(self, form):
        form.instance.movie = get_object_or_404(Movie, slug=self.kwargs['movie_slug'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('movies:detail', kwargs={'slug': self.object.movie.slug})


class ReviewUpdateView(SuccessMessageMixin, UpdateView):
    model = Review
    form_class = ReviewForm
    template_name = 'journal/review_form.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    success_message = "Review '%(title)s' was updated successfully."

    def get_success_url(self):
        return reverse_lazy('journal:review_detail', kwargs={'slug': self.object.slug})


class ReviewDeleteView(DeleteView):
    model = Review
    template_name = 'journal/review_confirm_delete.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def post(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(request, f"Review '{obj.title}' was deleted successfully.")
        return super().post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('movies:detail', kwargs={'slug': self.object.movie.slug})
