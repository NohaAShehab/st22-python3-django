from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignupCutomizedForm(UserCreationForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=255)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username','password1', 'password2']
