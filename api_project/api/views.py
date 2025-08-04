from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
"""using viewset"""
from rest_framework import viewsets

# view to list books
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer