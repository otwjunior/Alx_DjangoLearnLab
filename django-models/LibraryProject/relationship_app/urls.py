from django.urls import path
from .views import list_books, LibraryDetailView
#from .views import HelloView
urlpatterns = [
   path('books/', list_books, name= 'book-list'),
   path('listbooks/<str:name>/', LibraryDetailView.as_view(), name = 'available-books' ),
   
]