``` python

from bookshelf.models import Book
##create
bk1 = Book(title="1984", author="George Orwell", publication_year=1949)
bk1.save()