from django.shortcuts import render

# Create your views here.

# ## view --> list all courses
from courses.models import Course
from courses.forms import CourseModelForm

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class CoursesListView(ListView):
    model = Course   # get all objects --- send it to the template
    template_name = 'courses/index.html'



class CourseDetailView(DetailView):
    model = Course
    template_name =  'courses/show.html'


class CourseCreateView(CreateView):
    template_name = 'courses/create.html'
    success_url = '/courses/index'
    form_class = CourseModelForm


class CourseUpdateView(UpdateView):
    template_name = 'courses/edit.html'
    success_url = '/courses/index'
    form_class = CourseModelForm
    model = Course


class CourseDeleteView(DeleteView):
    template_name = 'courses/delete.html'
    model = Course
    success_url = '/courses/index'


