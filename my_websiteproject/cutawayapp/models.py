from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Blog(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, verbose_name='Название')
    text = models.TextField(default=None, verbose_name='Текст')
    image = models.ImageField(upload_to='image_blog/', blank=True, verbose_name='Фото')
    date = models.DateTimeField(verbose_name='Дата')
    comments = models.CharField(max_length=150,verbose_name='Коментарии',blank=True)

    def __str__(self):
        return self.name

