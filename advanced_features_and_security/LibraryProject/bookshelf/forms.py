<--! ExampleForm -->

from django import forms
from .models import Book
""" forms will handle user input validation """
class ExampleForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']


class ExampleForm(forms.Form):
    title = forms.CharField(max_length=100, label='Book Title')
    author = forms.CharField(max_length=100)
    publication_year = forms.IntegerField(label='Year Published')
