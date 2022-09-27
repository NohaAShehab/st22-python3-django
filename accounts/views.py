from django.shortcuts import render
from django.shortcuts import redirect, reverse
from django.urls import reverse_lazy
from django.http import  HttpResponse
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from accounts.forms import SignupCutomizedForm
# Create your views here.


def getProfile(request):
    # return HttpResponse("This my profile ")
    url = reverse('courses.index')
    return redirect(url)


class SignUpView(CreateView):
    form_class = SignupCutomizedForm
    success_url = reverse_lazy('login')
    template_name = 'registration/create.html'

