from django.urls import path, include
from courses.views import CoursesListView,CourseDetailView,\
   CourseCreateView, CourseUpdateView, CourseDeleteView

from django.contrib.auth.decorators import login_required
urlpatterns = [

   path('index', CoursesListView.as_view(), name='courses.index'),
   path('<int:pk>', CourseDetailView.as_view(), name='courses.show'),
   path('create', CourseCreateView.as_view(), name='courses.create'),
   path('<int:pk>/edit', CourseUpdateView.as_view(), name='courses.edit'),
   path('<int:pk>/delete',
        login_required(CourseDeleteView.as_view(), login_url='/accounts/login'), name='courses.delete'),


]
