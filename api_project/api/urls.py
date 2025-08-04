from django.urls import path, include
from .views import BookList
from rest_framework.routers import DefaultRouter
from .views import BookViewSet
"""token retrivval endpoint"""
from rest_framework.authtoken.views import obtain_auth_token

#settup routers
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),  # Maps to the BookList view
    path ('', include(router.urls)), #viewset routes here
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'), #token endpoint
]

