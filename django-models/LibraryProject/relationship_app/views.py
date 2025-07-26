from django.shortcuts import render, get_object_or_404
from .models import  Book, Library
from django.views.generic import DetailView 
# function based view
def book_list_view(request):
    books = Book.objects.all()
    return render (request, 'relationship_app/list_books.html',{'books': books})

#class based view
class LibraryDetailView(DetailView):
    model = Library
    template_name= "relationship_app/library_detail.html"
    context_object_name = 'library'

    # tell Django to use name field for the library
    slug_field = 'name' # field in model
    slug_url_kwarg = 'name' # keyword argument from URL

     


