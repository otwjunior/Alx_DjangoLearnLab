## delete
```python

bk1 = Book.objects.get(title="Nineteen Eighty-Four")
bk1.delete()

--Output
(1, {'bookshelf.Book': 1})