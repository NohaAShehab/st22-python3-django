from django.db import models

# Create your models here.
from django.shortcuts import  get_object_or_404, reverse

class Author(models.Model):
    name= models.CharField(max_length=100)
    bio = models.CharField(max_length=200, null=True, blank=True)
    city =models.CharField(max_length=200, null=True, blank=True)
    image= models.ImageField(upload_to="authors/images/")
    # # upload the file you select to folder media in the project
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


    @classmethod
    def get_authors(cls):
        return cls.objects.all()

    @classmethod
    def get_specific_author(cls, id):
        return get_object_or_404(cls,pk= id)


    def __str__(self):
        return f"{self.name}"

    def get_image_url(self):
        return f"/media/{self.image}"


    @classmethod
    def get_index_url(cls):
        return reverse("authors.index")


    def get_show_url(self):
        return reverse("authors.show", args=[self.id])

    def get_delete_url(self):
        return reverse("authors.delete", args=[self.id])
