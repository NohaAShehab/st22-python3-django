from django.shortcuts import render

# Create your views here.


def homepage(request):
    myflowers = ["Joury", "evorbia", "test", "abc"]
    myinfo = {"name":"noha", "track":"opensource"}
    return render(request, "flowers/homepage.html",
                  context={"flowers":myflowers, 'info':myinfo})

def indexView(request):
    return render(request, 'flowers/index.html')