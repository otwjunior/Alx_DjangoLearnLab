from django.urls import path
from . import views
from .views import list_books

#from .views import HelloVi
urlpatterns = [
   path('books/', views.list_books, name= 'book-list'),
   path('listbooks/<str:name>/', views.LibraryDetailView.as_view(), name = 'available-books' ),
   
   path('login/', views.CustomLoginView.as_view(template_name='relationship_app/login.html'), name = 'login'),
   path('logout/', views.CustomLogoutView.as_view(template_name='relationship_app/logout.html'), name ='logout'),
   path('register/', views.register, name = 'register'),
   path('', views.home_view, name='home'),
   
   # user path now
   path('admin-role/', views.admin_view, name='admin-view'),
   path('librarian-role/', views.librarian_view, name='librarian-view'),
   path('member-role/', views.member_view, name='member-view'),

   #  book operations urls 
   path('books/add_book/', views.add_book, name='add-book'),
    path('books/edit_book/<int:pk>/', views.update_book, name='update-book'),
    path('books/delete/<int:pk>/', views.delete_book, name='delete-book')
     
]