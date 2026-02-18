from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ['title', 'content', 'rating']

        labels = {
            'title': 'Review Title',
            'content': 'Your Thoughts',
            'rating': 'Rating (1.0 to 10.0)',
        }

        help_texts = {
            'title': 'Give your review a short descriptive title.',
            'content': 'Write your detailed opinion about the movie.',
            'rating': 'Use a decimal rating between 1.0 and 10.0.',
        }

        error_messages = {
            'title': {
                'required': 'Please enter a title for your review.',
                'max_length': 'The title is too long.',
            },
            'content': {
                'required': 'Please write your review content.',
            },
            'rating': {
                'required': 'Please provide a rating.',
                'invalid': 'Enter a valid decimal number.',
            },
        }

        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'e.g. Amazing movie!',
                'class': 'form-control',
            }),
            'content': forms.Textarea(attrs={
                'placeholder': 'Share your thoughts...',
                'class': 'form-control',
                'rows': 5,
            }),
            'rating': forms.NumberInput(attrs={
                'placeholder': 'e.g. 8.7',
                'class': 'form-control',
                'step': '0.5',
                'min': '1.0',
                'max': '10.0',
            }),
        }

    def clean_rating(self):
        rating = self.cleaned_data['rating']
        if rating < 1.0 or rating > 10.0:
            raise forms.ValidationError("Rating must be between 1.0 and 10.0.")
        return rating
