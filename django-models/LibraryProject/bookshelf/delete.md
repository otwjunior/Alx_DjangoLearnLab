## delete
```python
from bookshelf.models import Book

book= Book.objects.get(title="Ninteen Eighty-Four")
book.delete()