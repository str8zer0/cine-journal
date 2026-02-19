from django import forms
from django.utils import timezone
from library.models import MovieList, WatchPlan
from movies.models import Movie


class MovieListForm(forms.ModelForm):

    class Meta:
        model = MovieList
        fields = ['title', 'description', 'movies']

        labels = {
            'title': 'List Title',
            'description': 'Description',
            'movies': 'Movies in This List',
        }

        help_texts = {
            'title': 'Give your movie list a clear and descriptive name.',
            'description': 'Optionally describe the theme or purpose of this list.',
            'movies': 'Select one or more movies to include in this list.',
        }

        error_messages = {
            'title': {
                'required': 'Please enter a title for your movie list.',
                'max_length': 'The title is too long.',
            },
            'movies': {
                'required': 'Please select at least one movie.',
            },
        }

        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'e.g. My Favorite Sci‑Fi Movies',
                'class': 'form-control',
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Describe what this list is about...',
                'class': 'form-control',
                'rows': 4,
            }),
            'movies': forms.CheckboxSelectMultiple(attrs={
                'class': 'form-check-input',
            }),
        }



class WatchPlanForm(forms.ModelForm):
    movie_list = forms.ModelChoiceField(
        queryset=MovieList.objects.all(),
        required=False,
        label='Choose Existing Movie List',
        help_text='Select a predefined movie list for this plan.',
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    movies = forms.ModelMultipleChoiceField(
        queryset=Movie.objects.all(),
        required=False,
        label='Choose Movies Directly',
        help_text='Select one or more movies to automatically create a new list.',
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'})
    )

    class Meta:
        model = WatchPlan
        fields = ['title', 'planned_date', 'duration_hours', 'notes', 'movie_list', 'movies']

        labels = {
            'title': 'Plan Title',
            'planned_date': 'Planned Date',
            'duration_hours': 'Estimated Duration (hours)',
            'notes': 'Notes',
        }

        help_texts = {
            'title': 'Give your watch plan a short descriptive name.',
            'planned_date': 'Choose the date when you plan to watch these movies.',
            'duration_hours': 'Enter the total estimated duration in hours.',
            'notes': 'Optional notes about your plan.',
        }

        error_messages = {
            'title': {
                'required': 'Please enter a title for your watch plan.',
            },
            'planned_date': {
                'required': 'Please select a planned date.',
                'invalid': 'Enter a valid date.',
            },
            'duration_hours': {
                'required': 'Please enter the estimated duration.',
                'invalid': 'Enter a valid number.',
                'min_value': 'Duration must be a positive number.',
            },
        }

        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'e.g. Weekend Movie Marathon',
                'class': 'form-control',
            }),
            'planned_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
            }),
            'duration_hours': forms.NumberInput(attrs={
                'placeholder': 'e.g. 6',
                'class': 'form-control',
                'min': '1',
                'step': '0.5',
            }),
            'notes': forms.Textarea(attrs={
                'placeholder': 'Add any notes about your plan...',
                'class': 'form-control',
                'rows': 4,
            }),
        }

    def clean_planned_date(self):
        date = self.cleaned_data['planned_date']
        if date < timezone.now().date():
            raise forms.ValidationError("The planned date cannot be in the past.")
        return date
