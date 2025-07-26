from django.urls import path
from .views import LibraryDetailView, book_list_view
#from .views import HelloView
urlpatterns = [
   path('books/', book_list_view, name= 'book-list'),
   path('listbooks/<str:name>/', LibraryDetailView.as_view(), name = 'available-books' ),
   
]