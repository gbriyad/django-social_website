from django.contrib import admin

# Register your models here.
from images.models import Image


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['title','slug', 'image', 'created']
    list_filter =['created']