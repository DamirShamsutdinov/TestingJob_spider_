from django.db import models


class News(models.Model):
    """Модель объекта новостей"""

    title = models.CharField(max_length=255, verbose_name="Заголовок_новостей")
    datetime = models.DateTimeField(verbose_name="Дата&Время_новостей")
    tags = models.CharField(
        max_length=50, verbose_name="Теги_новостей", default="Yandex"
    )

    def __str__(self):
        return self.title
