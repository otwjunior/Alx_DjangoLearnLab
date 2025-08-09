from django.contrib import admin
from .models import Author, Book

# Show books inline when editing an author
class BookInline(admin.TabularInline):  # or admin.StackedInline for block layout
    model = Book
    extra = 1  # How many blank forms to show

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    inlines = [BookInline]  # Nested editing

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'publication_year', 'author')
    list_filter = ('publication_year', 'author')
    search_fields = ('title',)
