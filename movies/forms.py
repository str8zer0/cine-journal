from django import forms
from movies.models import Movie


class MovieForm(forms.ModelForm):

    class Meta:
        model = Movie
        fields = [
            'title',
            'description',
            'release_year',
            'cover',
            'imdb_link',
            'watched',
            'genres',
            'tags',
        ]

        labels = {
            'title': 'Movie Title',
            'description': 'Short Description',
            'release_year': 'Release Year',
            'cover': 'Cover Image',
            'imdb_link': 'IMDb Link',
            'watched': 'Already Watched',
            'genres': 'Genres',
            'tags': 'Tags',
        }

        help_texts = {
            'title': 'Enter the official title of the movie.',
            'description': 'Write a short summary or leave it empty.',
            'release_year': 'Year the movie was or will be released (must be after 1880).',
            'cover': 'Upload a poster or cover image.',
            'imdb_link': 'Paste the full IMDb URL (e.g., https://www.imdb.com/title/tt0468569/).',
            'genres': 'Select one or more genres.',
            'tags': 'Optional keywords to help categorize the movie.',
        }

        error_messages = {
            'title': {
                'required': 'Please enter the movie title.',
                'max_length': 'The title is too long.',
            },
            'release_year': {
                'required': 'Please enter the release year.',
                'invalid': 'Enter a valid year.',
            },
            'imdb_link': {
                'invalid': 'Please enter a valid URL.',
            },
        }

        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'e.g. The Dark Knight',
                'class': 'form-control',
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Write a short description...',
                'class': 'form-control',
                'rows': 4,
            }),
            'release_year': forms.NumberInput(attrs={
                'placeholder': 'e.g. 2008',
                'class': 'form-control',
            }),
            'imdb_link': forms.URLInput(attrs={
                'placeholder': 'https://www.imdb.com/title/tt0468569/',
                'class': 'form-control',
            }),
            'genres': forms.CheckboxSelectMultiple(attrs={
                'class': 'form-check-input',
            }),
            'tags': forms.CheckboxSelectMultiple(attrs={
                'class': 'form-check-input',
            }),
        }

    def clean_release_year(self):
        year = self.cleaned_data['release_year']
        if year < 1880:
            raise forms.ValidationError("Movies did not existed before 1880.")
        return year
