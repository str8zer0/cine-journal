from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from library.models import MovieList, WatchPlan


class MovieListListView(ListView):
    queryset = MovieList.objects.prefetch_related('movies')
    template_name = 'library/movielist_list.html'
    context_object_name = 'lists'
    ordering = ['-created_at']


class MovieListDetailView(DetailView):
    queryset = MovieList.objects.prefetch_related('movies')
    template_name = 'library/movielist_detail.html'
    context_object_name = 'list'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'


class MovieListCreateView(SuccessMessageMixin, CreateView):
    model = MovieList
    form_class = MovieListForm
    template_name = 'library/movielist_form.html'
    success_message = "Movie list '%(title)s' was created successfully."

    def get_success_url(self):
        return reverse_lazy('movielist_detail', kwargs={'slug': self.object.slug})


class MovieListUpdateView(SuccessMessageMixin, UpdateView):
    model = MovieList
    form_class = MovieListForm
    template_name = 'library/movielist_form.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    success_message = "Movie list '%(title)s' was updated successfully."

    def get_success_url(self):
        return reverse_lazy('movielist_detail', kwargs={'slug': self.object.slug})


class MovieListDeleteView(DeleteView):
    model = MovieList
    template_name = 'library/movielist_confirm_delete.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    success_url = reverse_lazy('movielist_list')

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(request, f"Movie list '{obj.title}' was deleted successfully.")
        return super().delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('movielist_detail', kwargs={'slug': self.object.movie_list.slug})


class WatchPlanListView(ListView):
    queryset = WatchPlan.objects.select_related('movie_list')
    template_name = 'library/watchplan_list.html'
    context_object_name = 'plans'
    ordering = ['planned_date']


class WatchPlanDetailView(DetailView):
    model = WatchPlan
    template_name = 'library/watchplan_detail.html'
    context_object_name = 'plan'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_queryset(self):
        return WatchPlan.objects.select_related('movie_list')


class WatchPlanCreateView(SuccessMessageMixin, CreateView):
    model = WatchPlan
    form_class = WatchPlanForm
    template_name = 'library/watchplan_form.html'
    success_message = "Watch plan '%(title)s' was created successfully."

    def form_valid(self, form):
        movie_list = form.cleaned_data.get('movie_list')
        movies = form.cleaned_data.get('movies')

        if movie_list:
            form.instance.movie_list = movie_list

        elif movies:
            auto_list = MovieList.objects.create(
                title=form.cleaned_data['title'],
                description=f"Automatically generated list for {form.cleaned_data['title']}",
            )
            auto_list.movies.set(movies)
            form.instance.movie_list = auto_list

        response = super().form_valid(form)

        if self.object.exceeds_available_time():
            messages.warning(
                self.request,
                "Warning: Your selected movies may exceed your planned watch duration."
            )

        return response

    def get_success_url(self):
        return reverse_lazy('watchplan_detail', kwargs={'slug': self.object.slug})


class WatchPlanUpdateView(SuccessMessageMixin, UpdateView):
    model = WatchPlan
    form_class = WatchPlanForm
    template_name = 'library/watchplan_form.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    success_message = "Watch plan '%(title)s' was updated successfully."

    def get_success_url(self):
        return reverse_lazy('watchplan_detail', kwargs={'slug': self.object.slug})


class WatchPlanDeleteView(DeleteView):
    model = WatchPlan
    template_name = 'library/watchplan_confirm_delete.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(request, f"Watch plan '{obj.title}' was deleted successfully.")
        return super().delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('watchplan_detail', kwargs={'slug': self.object.watch_plan.slug})
