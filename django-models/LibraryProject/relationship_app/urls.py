from django.urls import path
from .views import (
   list_books,
   LibraryDetailView, 
   CustomLoginView,
   RegisterView,
   CustomLogoutView,
   home_view
)
#from .views import HelloVi
urlpatterns = [
   path('books/', list_books, name= 'book-list'),
   path('listbooks/<str:name>/', LibraryDetailView.as_view(), name = 'available-books' ),
   
   path('login/', CustomLoginView.as_view(), name = 'login'),
   path('logout/', CustomLogoutView.as_view(), name ='logout'),
   path('register/', RegisterView.as_view(), name = 'register'),
   path('', home_view, name='home'),

]