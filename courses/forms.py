from django import forms
from courses.models import Course
class CourseModelForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'