from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from cutawayapp.models import Blog
from cutawayapp.forms import BlogForm, UserForm


# Create your views here.

def home(request):
    return render(request, 'cutaway/home.html', {})


@login_required(login_url='/mywebsite/sign-in/')
def algorithms(request):
    return render(request, 'cutaway/algorithms.html', {})


@login_required(login_url='/mywebsite/sign-in/')
def blog(request):
    posts = Blog.objects.all().order_by('name')
    return render(request, 'cutaway/blog.html', {
        'posts': posts
    })


def do_post(request):
    blog_form = BlogForm

    if request.method == 'POST':
        blog_form = BlogForm(request.POST, request.FILES)
        if blog_form.is_valid():
            blog_form.save()
            return HttpResponseRedirect('{}?sent=True'.format(reverse('blog')))

    return render(request, 'cutaway/do_post.html', {
        'blog_form': blog_form,
        'sent': request.GET.get('sent', False)
    })


def sign_up(request):
    user_form = UserForm()

    if request.method == 'POST':
        user_form = UserForm(request.POST)

        if user_form.is_valid():
            new_user = User.objects.create_user(**user_form.cleaned_data)
            new_user.save()

            login(request,authenticate(
                username=user_form.cleaned_data['username'],
                password=user_form.cleaned_data['password']
            ))

            return redirect(home)

    return render(request, 'cutaway/sign_up.html', {
        'user_form': user_form
    })
