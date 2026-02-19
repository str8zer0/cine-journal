from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from journal.forms import ReviewForm
from journal.models import Review
from movies.models import Movie


class ReviewListView(ListView):
    queryset = Review.objects.select_related('movie')
    template_name = 'journal/review_list.html'
    context_object_name = 'reviews'
    ordering = ['-created_at']


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

    def form_valid(self, form):
        movie_slug = self.kwargs.get('movie_slug')
        form.instance.movie = Movie.objects.get(slug=movie_slug)
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
