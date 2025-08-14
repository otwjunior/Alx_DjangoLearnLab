from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer
from rest_framework.generics import (ListAPIView, RetrieveAPIView,CreateAPIView,UpdateAPIView,DestroyAPIView)
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
"""implemting custom views for book model"""
#list all books
class BookListView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    #onlyauthenticated user can view book catalog
    permission_classes= [IsAuthenticatedOrReadOnly]
    #filtering displayed book details
    filter_backends =[DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields = ['title','author','publication_year']
    #ordering  by title and publication_year
    ordering_fields= ['title', 'publication_year']
    #filtering by search
    search_fields =['title','author__name']
#view single book
class BookDetailView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    #onlyauthenticated user can request a book
    permission_classes= [IsAuthenticatedOrReadOnly]
    #implemeting search filters
    filter_backends =[filters.SearchFilter]
    search_fields =['title','author']
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