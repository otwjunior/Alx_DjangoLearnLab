from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required, login_required
from .forms import ExampleForm, BookForm
from .models import Book

# edit a book
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)    
    return render (request, 'bookshelf/book_edit.html', {'form':form})

# add book view   
@permission_required('bookshelf.can_create', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    
    return render(request, 'bookshelf/add_book.html', {'form':form})

#deletion view
@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'bookshelf/book_delete.html', {'book':book})

#view books
@login_required
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

#example view
def example_form_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Process the data in form.cleaned_data dictionary
            title = form.cleaned_data['title']
            author = form.cleaned_data['author']
            year = form.cleaned_data['publication_year']
            
            # For example, just print or do something with data
            print(f"Book: {title}, Author: {author}, Year: {year}")
            
            return redirect('some_view_name')  # redirect after successful POST
    else:
        form = ExampleForm()

    return render(request, 'bookshelf/form_example.html', {'form': form})
