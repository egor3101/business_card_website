from django.db import models


# Create your models here.

class Blog(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    image = models.ImageField(upload_to='image_blog/', blank=True, verbose_name='Фото')
    text = models.TextField(default=None, verbose_name='Текст')
    date = models.DateTimeField(verbose_name='Дата')

    def __str__(self):
        return self.name
