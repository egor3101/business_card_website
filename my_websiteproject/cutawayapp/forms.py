from django.contrib.auth.models import User
from django import forms
from cutawayapp.models import Blog


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('name', 'image', 'text', 'date')


class UserForm(forms.ModelForm):
    email = forms.CharField(max_length=100, required=True)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'email')
