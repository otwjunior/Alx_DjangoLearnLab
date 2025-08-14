from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer
from rest_framework.generics import (ListAPIView, RetrieveAPIView,CreateAPIView,UpdateAPIView,DestroyAPIView)
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
"""implemting custom views for book model"""
#list all books
class BookListView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    #onlyauthenticated user can view book catalog
    permission_classes= [IsAuthenticatedOrReadOnly]
#view single book
class BookDetailView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    #onlyauthenticated user can request a book
    permission_classes= [IsAuthenticatedOrReadOnly]
#add a book
class BookCreateView(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    #ensure only authenticated user can add abook
    permission_classes = [IsAuthenticated]
#delete a book
class BookDeleteView(DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    #onlyauthenticated user can delete
    permission_classes= [IsAuthenticated]
#update book
class BookUpdateView(UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    #only authenticated user can modify
    permission_classes= [IsAuthenticated]