
from django.urls import path
from books.views import helloWorld, sayWelcome, sayHi, homepage,\
    indexView, showbook, booksindex_model, get_book_from_db,\
    createBook,deleteBook, editBook
urlpatterns = [
    path('hello', helloWorld, name='helleworld'),
    path('welcome', sayWelcome, name='saywelcome'),
    path('hi/<username>', sayHi, name='sayhi'),
    path('home',homepage, name='home'),
    path('index',indexView, name='books.index'),
    path('show/<int:id>',showbook, name='books.show'),
    path('db/index', booksindex_model, name='db_books.index'),
    path('db/<int:id>', get_book_from_db,name= 'db_books.show'),
    path('create',createBook, name='books.create' ),
    path('delete/<int:id>', deleteBook, name='db_books.delete'),
    path('edit/<int:id>', editBook, name='db_books.edit'),

]
