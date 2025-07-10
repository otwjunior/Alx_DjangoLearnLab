## update
```python

bk1 = Book.objects.get(title=1984)
bk1.title = "Nineteen Eighty-Four"
bk1.save()