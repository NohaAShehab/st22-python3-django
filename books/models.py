from django.db import models
from django.shortcuts import reverse, get_object_or_404


# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200, null=True)
    no_of_pages = models.IntegerField(default=0)
    image = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'

    @classmethod
    def get_all_books(cls):
        return cls.objects.all()

    @classmethod
    def get_specific_book(cls, book_id):
        # return cls.objects.get(id=book_id)
        return get_object_or_404(cls, pk=book_id)

    def get_show_url(self):
        return reverse("db_books.show", args=[self.id])

    @classmethod
    def get_index_url(cls):
        return reverse("db_books.index")


    def get_delete_url(self):
        return reverse("db_books.delete", args=[self.id])
