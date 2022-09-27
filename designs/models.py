from django.db import models
from django.shortcuts import reverse, get_object_or_404
# Create your models here.

## model 000> represent table in database


class Designer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Design(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='designs/images/', blank=True, null=True)
    description = models.CharField(max_length=200)
    price = models.IntegerField(default=10)
    designer= models.ForeignKey(Designer, on_delete=models.CASCADE,
                                null=True, blank=True, related_name='design_owner')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @classmethod
    def get_index_url(cls):
        return reverse("designs.index")

    def __str__(self):
        return f"{self.name}"


    @classmethod
    def get_all_designs(cls):
        return cls.objects.all()


    def get_image_url(self):
        return f'/media/{self.image}'

    @classmethod
    def get_specific_design(cls, id):
        return get_object_or_404(cls, pk=id)


    def get_edit_url(self):
        return reverse("designs.edit", args=[self.id])



