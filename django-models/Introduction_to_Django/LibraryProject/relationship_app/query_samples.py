import os
import django

# Setup Django environment for standalone script
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings')  # Replace with your project name
django.setup()

from relationship_app.models import Author, Book, Library

def query_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
    except Author.DoesNotExist:
        print(f"No author found with name: {author_name}")
        return

    books = Book.objects.filter(authors=author)
    print(f"Books by {author_name}:")
    for book in books:
        print(f" - {book.title}")

def list_all_books():
    books = Book.objects.all()
    print("All books in the library system:")
    for book in books:
        print(f" - {book.title}")

def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
    except Library.DoesNotExist:
        print(f"No library found with name: {library_name}")
        return

    if library.librarian:
        print(f"Librarian for {library_name}: {library.librarian.name}")
    else:
        print(f"No librarian assigned to {library_name}")

if __name__ == "__main__":
    # Replace these with actual values for testing
    query_books_by_author("Alice")
    print()
    list_all_books()
    print()
    get_librarian_for_library("Central Library")
