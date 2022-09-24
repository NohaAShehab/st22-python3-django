from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
### views can be created in form of functions /classes


def helloWorld(request):
    return HttpResponse("------Hello world-----")


def sayWelcome(request):
    return HttpResponse("<h1> Welcome, Nice to meet you </h1>")


def sayHi(request, username):
    return HttpResponse(f"<h1 style='color:red'> Hi {username}</h1>")


def homepage(request):
    return render(request, "books/homepage.html")