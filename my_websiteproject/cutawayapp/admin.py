from django.contrib import admin
from cutawayapp.models import Blog


# Register your models here.


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['name', 'text', 'image', 'date']
