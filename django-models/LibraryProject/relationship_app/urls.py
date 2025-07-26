from django.urls import path
from . import views
#from .views import HelloVi
urlpatterns = [
   path('books/', list_books, name= 'book-list'),
   path('listbooks/<str:name>/', LibraryDetailView.as_view(), name = 'available-books' ),
   
   path('login/', CustomLoginView.as_view(template_name='relationship_app/login.html'), name = 'login'),
   path('logout/', CustomLogoutView.as_view(template_name='relationship_app/logout.html'), name ='logout'),
   path('register/', views.register, name = 'register'),
   path('', home_view, name='home'),

]