import re
from django import forms
from movies.models import Movie, Genre, Tag


class MovieForm(forms.ModelForm):
    slug = forms.SlugField(
        required=False,
        disabled=True,
        label='URL Slug',
        help_text='Auto-generated from title.',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

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
            'slug',
        ]

        labels = {
            'title': 'Movie Title',
            'slug': '',
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
            'description': 'Write a short summary or leave it empty. (optional)',
            'release_year': 'Year the movie was or will be released (must be after 1880).',
            'cover': 'Upload a poster or cover image. (optional)',
            'imdb_link': 'Paste the full IMDb URL. (optional).',
            'genres': 'Select one or more genres.',
            'tags': 'Select one or more tags. (optional)',
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

    def clean_imdb_link(self):
        url = self.cleaned_data.get('imdb_link')

        if not url:
            return url  # field is optional

        pattern = r"^https?://(www\.|m\.)?imdb\.com/title/tt\d+"

        if not re.match(pattern, url):
            raise forms.ValidationError("Please enter a valid IMDb movie URL or leave the field blank.")

        return url


    def clean_release_year(self):
        year = self.cleaned_data['release_year']
        if year < 1880:
            raise forms.ValidationError("Movies did not exist before 1880.")
        return year


class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['name']
        labels = {'name': 'Genre Name'}
        help_texts = {'name': 'A stylistic or thematic movie category'}
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control'})}


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']
        labels = {'name': 'Tag Name'}
        help_texts = {'name': 'A keyword to help categorize the movie.'}
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control'})}
