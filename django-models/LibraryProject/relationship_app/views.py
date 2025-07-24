from django.shortcuts import render
from .models import  Book, Library
from django.views.generic import DetailView 
# function based view
def book_list_view(request):
    books = Book.objects.select_related('author').all()
    return render (request, 'relationship_app/list_books.html',{'books': books})

#class based view
class LibraryDetailView(DetailView):
    model = Library
    template_name= "relationship_app/library_detail.html"
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Fetch books related to this library
        context['books'] = self.object.books.all()
        return context
