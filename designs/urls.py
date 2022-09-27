from django.urls import path, include
from designs.views import designIndexView, createDesignView, editDesignView
urlpatterns = [

    path('index', designIndexView, name='designs.index'),
    path('create',createDesignView, name='designs.create' ),
    path('edit/<int:id>',editDesignView, name='designs.edit' ),

]
