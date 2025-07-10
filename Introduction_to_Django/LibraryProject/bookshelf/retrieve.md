## retrieve
```python

books = Book.objects.all()
for bk in books:
...    print(bk.title,bk.author,bk.publication_year)

Output
1984 George Orwell 1949
