
from django.urls import path, include
from authors.views import  indexView, createAuthorView, showAuthorView,deleteAuthor
urlpatterns = [

    path("index", indexView, name='authors.index'),
    path("create", createAuthorView, name='authors.create'),
    path("<int:id>", showAuthorView, name='authors.show'),
    path("delete/<int:id>", deleteAuthor, name='authors.delete'),


]