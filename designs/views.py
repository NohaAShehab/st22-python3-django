from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
from designs.models import Design
from designs.forms import DesignForm, DesignModelForm

def designIndexView(request):
    designs = Design.get_all_designs()
    return render(request, "designs/index.html", context={"designs":designs})


# def createDesignView(request):
#     if request.POST:
#         design = Design()
#         design.name= request.POST["name"]
#         if request.FILES:
#             design.image = request.FILES['image']
#         design.price = request.POST["price"]
#         design.description = request.POST["description"]
#
#         design.save()
#         url = Design.get_index_url()
#         return redirect(url)
#
#         ###
#     form = DesignForm()
#     return render(request, 'designs/create.html', context={"form":form})












#
# def editDesignView(request, id):
#     selected_design = Design.get_specific_design(id)
#     if request.POST:
#         selected_design.name= request.POST["name"]
#         if request.FILES:
#             selected_design.image = request.FILES['image']
#         selected_design.price = request.POST["price"]
#         selected_design.description = request.POST["description"]
#
#         selected_design.save()
#         url = Design.get_index_url()
#         return redirect(url)
#
#         ########################
#     form = DesignModelForm(instance=selected_design)
#     return render(request, 'designs/edit.html',
#                   context={"form":form,'design': selected_design})




@login_required(login_url='/accounts/login')
def editDesignView(request, id):
    selected_design = Design.get_specific_design(id)
    if request.POST:
        myform = DesignModelForm(request.POST, request.FILES,
                                 instance=selected_design)
        if myform.is_valid():
            myform.save()
            url = Design.get_index_url()
            return redirect(url)

        return render(request, 'designs/edit.html',
                      context={"form": myform, 'design': selected_design})
        ########################
    form = DesignModelForm(instance=selected_design)
    return render(request, 'designs/edit.html',
                  context={"form":form,'design': selected_design})





def createDesignView(request):
    if request.POST:
        myform = DesignModelForm(request.POST, request.FILES)
        if myform.is_valid():
            myform.save()
            url = Design.get_index_url()
            return redirect(url)

        ###
    form = DesignModelForm()
    return render(request, 'designs/create.html', context={"form":form})








