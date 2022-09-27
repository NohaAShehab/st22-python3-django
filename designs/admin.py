from django.contrib import admin

# Register your models here.
from designs.models import Design, Designer

admin.site.register(Design)
admin.site.register(Designer)