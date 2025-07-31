<--! ExampleForm -->

from django import forms
from .models import Book
""" forms will handle user input validation """
class ExampleForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']