

from django.urls import path, include
from  accounts.views import getProfile,SignUpView
urlpatterns = [

    path('profile/',getProfile, name='userprofile'),
    path('signup',SignUpView.as_view(), name='signup')


]