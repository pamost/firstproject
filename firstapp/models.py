from django.db import models

class PizzaShop(models.Model):
    name=models.CharField(max_length=30, verbose_name='Пиццерия')
    description = models.TextField(verbose_name='Описание')
    rating = models.FloatField(default=0, verbose_name='Рейтинг')
    url = models.URLField(verbose_name='Сайт пиццерии')

    def __str__(self):
        return self.name