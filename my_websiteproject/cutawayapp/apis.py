from django.http import JsonResponse

from .models import Blog
from cutawayapp.serializers import BlogSerializers


def client_get_posts(request):
    posts = BlogSerializers(
        Blog.objects.all().order_by("-id"),
        many=True,
        context = {'request': request}
    ).data

    return JsonResponse({'post': posts})
