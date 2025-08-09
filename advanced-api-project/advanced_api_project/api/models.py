from django.db import models

#author model
class Author(models.Model):
    name = models.CharField(max_length=30)

# book model
class Book(models.Model):
    title = models.CharField(max_length=20)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='book' )
    publication_year = models.IntegerField()
