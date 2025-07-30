import os 
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author,Book,Library, Librarian

def query_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        for book in books:
            print(book.title)
    except Author.DoesNotExist:
        print(f"no author with the name '{author_name}'")

def list_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        for  book in books:
            print(book.title)
    except Library.DoesNotExist:
        print('that library does not exist')

def get_librarian_for_library(library_name):
    library = Library.objects.get(name = library_name)
    librarian = Librarian.objects.get(library=library)
    print(librarian)

if __name__ == "__main__":
    query_books_by_author('Author Name')
    list_books_in_library('central Library')
    get_librarian_for_library('central liibrary')
