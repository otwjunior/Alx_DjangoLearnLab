
``` python

from bookshelf.models import Book
##create
bk1 = Book(title="1984", author="George Orwell", publication_year=1949)
bk1.save()

## retrieve
books = Book.objects.all()
for bk in books:
...    print(bk.title,bk.author,bk.publication_year)

Output
1984 George Orwell 1949

## update
bk1 = Book.objects.get(title=1984)
bk1.title='Nineteen Eighty-Four'
bk1.save()

## delete
bk1 = Book.objects.get(title="Nineteen Eighty-Four")
bk1.delete()

--Output
(1, {'bookshelf.Book': 1})
