from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'cutaway/home.html', {})


def algorithms(request):
    return render(request, 'cutaway/algorithms.html', {})


def blog(request):
    return render(request, 'cutaway/blog.html', {})
