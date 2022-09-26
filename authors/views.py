from django.shortcuts import render , redirect
# Create your views here.

from authors.models import Author
def indexView(request):
    allauthors = Author.get_authors()
    return render(request,'authors/index.html', context={"authors":allauthors})


def createAuthorView(request):
    if request.POST:
        author =Author()
        author.name =request.POST["name"]
        author.city = request.POST["city"]
        author.bio = request.POST["bio"]
        ### image ---> request.FILES
        author.image = request.FILES["image"]
        author.save()
        url = Author.get_index_url()
        return redirect(url)

    return render(request, "authors/create.html")


def showAuthorView(request, id):
    author = Author.get_specific_author(id)
    return render(request,"authors/show.html", context={'author':author})

def deleteAuthor(request, id):
    author = Author.get_specific_author(id)
    author.delete()
    return redirect(Author.get_index_url())