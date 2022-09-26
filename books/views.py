from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
# Create your views here.
### views can be created in form of functions /classes
from books.models import Book
from authors.models import Author
def helloWorld(request):
    return HttpResponse("------Hello world-----")


def sayWelcome(request):
    return HttpResponse("<h1> Welcome, Nice to meet you </h1>")


def sayHi(request, username):
    return HttpResponse(f"<h1 style='color:red'> Hi {username}</h1>")


def homepage(request):
    return render(request, "books/homepage.html")


bookslist = [
        {'id':1,'title':'book1', 'description':'book1 description', 'image':'pic1.png'},
        {'id':2,'title': 'book2', 'description': 'book2 description', 'image': 'pic2.png'},
        {'id':3,'title': 'book3', 'description': 'book3 description', 'image': 'pic3.png'},
        {'id':4,'title': 'book4', 'description': 'book4 description', 'image': 'pic4.png'}

    ]

def indexView(request):
    return render(request,"books/index.html", context={"books":bookslist} )


def showbook(request,id):
    print(type(id))
    for book in bookslist:
        if book['id']==id:
            return render(request, 'books/showbook.html', context={"book":book})
    else:
        return HttpResponse("Book not found")



def booksindex_model(request):
    ## get data from the datbase
    books = Book.get_all_books()
    ## display in the books.html
    return render(request, 'books/books_index.html', context={"books":books})



def get_book_from_db(request, id): # get request
    book = Book.get_specific_book(id)
    return render(request, 'books/showbook_db.html', context={"book":book})


def createBook(request):
    if request.POST:
        # return HttpResponse('Post request received')
        title = request.POST["title"]
        description= request.POST["description"]
        no_of_pages = request.POST["no_of_pages"]
        image = request.POST["image"]

        book = Book()
        book.title= title
        book.description = description
        book.no_of_pages = no_of_pages
        book.image = image
        if request.POST["author"]:
            author = Author.get_specific_author(request.POST["author"])
            book.author = author
        # print(request.POST["author"])
        book.save()
        # return HttpResponse("book added")
        url = Book.get_index_url()
        return redirect(url)


    authors= Author.get_authors()
    return render(request,"books/createbook.html", context={'authors':authors})



def deleteBook(request, id):
    book = get_object_or_404(Book, pk=id)
    book.delete()
    url = Book.get_index_url()
    return redirect(url)




def editBook(request, id):
    select_book= Book.get_specific_book(id)

    if request.POST:
        select_book.title = request.POST["title"]
        select_book.description = request.POST["description"]
        select_book.image = request.POST["image"]
        select_book.no_of_pages = request.POST["no_of_pages"]

        if request.POST["author"]:
            author = Author.get_specific_author(request.POST["author"])
            select_book.author = author


        select_book.save()
        url = select_book.get_show_url()
        return redirect(url)

    authors = Author.get_authors()
    return  render(request, "books/editbook.html",
                   context={"book":select_book, "authors":authors})






