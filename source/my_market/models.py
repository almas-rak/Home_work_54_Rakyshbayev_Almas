from django.db import models


# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=50, verbose_name='Категория')
    description = models.CharField(max_length=200, blank=True, null=True, verbose_name='Описание')


class Product(models.Model):
    product_name = models.CharField(max_length=50, verbose_name='Продукт')
    category = models.ForeignKey()
    add_date_time = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время добавления')
    price = models.DecimalField(verbose_name='Стоимость')
    image = models.ImageField()
