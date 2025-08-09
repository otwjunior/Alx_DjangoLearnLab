from rest_framework import serializers
from .models import Book, Author

"""book serializer for all fields"""
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title','author', 'publication_year']
    #ensure publicatin year not in future
    def validate_publication_year(self, value):
        if value > 2025:
            raise serializers.ValidationError("book can't have future date") 
        return value
#serialize author
class AuthorSerializer(serializers.ModelSerializer):
    #nested book serializer to include book by author
    books = BookSerializer(many=True)

    class Meta:
        model = Author
        fields = ['name', 'books']