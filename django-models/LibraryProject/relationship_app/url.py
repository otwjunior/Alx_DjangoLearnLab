from django.urls import path
from . import views

urlpatterns = [
    path('books/', book_list_view, name= 'book-list'),
    path('listbooks/',library_view, name = 'available-books' ),
]