## retrieve
```python
from bookshelf.models import Book

bk1 == Book.objects.get(title=1984)
print(bk1.title, bk1.author, bk1.publication_year)
Output
1984 George Orwell 1949
