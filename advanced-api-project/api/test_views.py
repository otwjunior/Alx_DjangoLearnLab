from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Book, Author
from django.contrib.auth.models import User

# Create your tests here.
'''check it test mechanism works'''
class SimpleTestCase(TestCase):
    def test_example(self):
        self.assertEqual(1+1, 2)
#test for book model

class BookModelTestCase(TestCase):
    def setUp(self):
        #initiate test data, runs before each test
        self.client =APIClient()
        self.user =User.objects.create_user(username="testuser",password="testpass")#dump credetials
        self.client.login(username='testuser', password='testpass')#authenicate client
        self.author = Author.objects.create(name="Tom Reddington")
        self.book_data = {
            "title": "Blacklist",
            "author" : "Tom Reddington",
            "publication_year": 2009
        }
    #NOW THE TEST 
    def test_create_book(self):
        #check of book was created correctly
        response = self.client.post("/books/create/", self.book_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)#book created succefully
        self.assertEqual(Book.objects.count(), 1)# book exist in db
        self.assertEqual(Book.objects.get().title, "Blacklist")# the title is correct
    #get test  to list books
    def test_get_books(self):
        #create abook in test db
        Book.objects.create(
            title="Blacklist",
            author=self.author,
            publication_year=2009
        )
        #make get request to feth all books
        response = self.client.get("http://127.0.0.1:8000/books/")
        #check if request was succeful
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        #check that exatly one boook returned
        self.assertEqual(len(response.data), 1)
        #check that book data matches
        self.assertEqual(response.data[0]['title'], "Blacklist")
        self.assertEqual(response.data[0]['publication_year'], 2009)
        # if serialized return author as id
        self.assertEqual(response.data[0]['author'], self.author.name)
    #updating book test
    def test_updating_book(self):
        #initial book details
        Book.objects.create(
            title="Blacklist",
            author=self.author,
            publication_year=2009
        )
        updated_date = {
            "title": "Blacklist Redemption",
            "author": self.author.id,
            "publication_year": 2024
        }
        response = self.client.put(f"/books/update/", updated_data, format="json")

        self.assertEqual(responses.status_code, status.HTTP_200_OK)
        book.refresh_from_db() 
        self.assertEqual(book.title, "Blacklist Redemption")
    #delteing book test
    def test_delete_book(self):
        # first log in the test user
        self.client.login(username="testuser",password="testpass")
        #create a book to delete
        book = Book.objects.create(
            title="Blacklist",
            author=self.author,
            publication_year=2009
        )
        response = self.client.delete(f"/book/delete/{book.id}/")

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)# no book left