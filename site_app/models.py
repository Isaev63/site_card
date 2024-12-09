from django.db import models


class FeatureCard(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    image = models.ImageField(upload_to='img_card/', verbose_name='Изображение')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.title
