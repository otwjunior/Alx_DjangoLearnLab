from rest_framework import  serializers
from .models import Book, Author

''' create custom serialzer fro the models'''
 
#custom book serializer
class BookSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='name',      # use the name field
        queryset=Author.objects.all()
    )
    
    class Meta:
        model =  Book
        fields = '__all__'
        #custom validation
    def validate_publication_year(self, value):
        from datetime import date
        current_year = date.today().year
        if value > current_year:
            raise serializers.ValidationError('future date are not logically correct')
        return value
# custom author serializer
class AuthorSerializer(serializers.ModelSerializer):
    
    # nest with  book serializer
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']
