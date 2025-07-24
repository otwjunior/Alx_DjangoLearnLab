from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=30)
    author =models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return f"{self.title} by {self.author.name}"

class Library(models.Model):
    name = models.CharField(max_length=20)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return f"{self.name} has {self.book.title}"

class Librarian(models.Model):
    name = models.CharField(max_length=20)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} serves at {self.library}"