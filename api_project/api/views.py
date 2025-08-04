from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
"""using viewset"""
from rest_framework import viewsets
"""add permission to book views"""
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

# view to list books
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes=[IsAuthenticated] #user need tobe auth to view books
    authentication_classes = [TokenAuthentication] # user need tokens to authenticate