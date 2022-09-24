
from django.urls import path
from books.views import helloWorld, sayWelcome, sayHi, homepage
urlpatterns = [
    path('hello', helloWorld, name='helleworld'),
    path('welcome', sayWelcome, name='saywelcome'),
    path('hi/<username>', sayHi, name='sayhi'),
    path('home',homepage, name='home'),

]
