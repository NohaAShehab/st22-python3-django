from django.db import models
from django.shortcuts import reverse
# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=100)
    max_grade = models.IntegerField(default=100)
    image = models.ImageField(upload_to='courses/images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{self.name}'


    def get_image_url(self):
        return f'/media/{self.image}'

    def get_show_url(self):
        return reverse('courses.show', args=[self.id])

    def get_edit_url(self):
        return reverse('courses.edit', args=[self.id])

    def get_delete_url(self):
        return reverse('courses.delete', args=[self.id])
