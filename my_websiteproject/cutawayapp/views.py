from django.shortcuts import render, redirect

from cutawayapp.models import Blog
from cutawayapp.forms import BlogForm

from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.

def home(request):
    return render(request, 'cutaway/home.html', {})


def algorithms(request):
    return render(request, 'cutaway/algorithms.html', {})


def blog(request):
    return render(request, 'cutaway/blog.html', {})


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
