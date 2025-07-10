## update
```python

bk1 = Book.objects.get(title=1984)
bk1.title = "Nineteen Eighty-four"
bk1.save()