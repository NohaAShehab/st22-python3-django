from django.urls import path
from flowers.views import homepage as flowershomepage
from flowers.views import  indexView
urlpatterns = [
    path('home', flowershomepage, name='flowershomepage'),
    path('index', indexView, name= 'flowers.index')

]
