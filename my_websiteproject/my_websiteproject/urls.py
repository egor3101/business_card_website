"""my_websiteproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls.static import static
from django.conf import settings

from cutawayapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('mywebsite/algorithms', views.algorithms, name='algorithms'),
    path('mywebsite/blog', views.blog, name='blog'),
    path('mywebsite/sign-in/', LoginView.as_view(template_name='cutaway/sign_in.html'),
        name='mywebsite-sign-in'),
    path('mywebsite/logout/', LogoutView.as_view(next_page='/'),
       name='mywebsite-sign-out'),
    path('mywebsite/do_post', views.do_post, name='do_post'),
    path('mywebsite/sign-up', views.sign_up, name='sign-up')
] + static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
