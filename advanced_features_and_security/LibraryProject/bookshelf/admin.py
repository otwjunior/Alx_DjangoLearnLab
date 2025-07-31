from django.contrib import admin
from .models import Book
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
# Register your models here.
class BookAdmin(admin.ModelAdmin):
    #define what field we want to display in a list
    list_display = ('title', 'author', 'publication_year')
    #add filters on specific  field to make searching easiaer
    list_filter = ('author', 'publication_year')
    #enable search on specific fields
    search_fields = ('title', 'author')

#register custom admin class
admin.site.register(Book, BookAdmin)
admin.site.register(CustomUser)