from django.contrib.auth.models import User
from django import forms
from cutawayapp.models import Blog


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('name', 'image', 'text', 'date')
