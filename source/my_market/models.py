from django.db import models


# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=50, db_index=True, verbose_name='Категория')
    description = models.CharField(max_length=200, blank=True, null=True, verbose_name='Описание')

    def __str__(self):
        return f'{self.category_name}'


class Product(models.Model):
    product_name = models.CharField(max_length=50, verbose_name='Продукт')
    description = models.TextField(max_length=2000, blank=True, null=True, verbose_name='Описание')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='category')
    add_date_time = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время добавления')
    price = models.DecimalField(max_digits=11, decimal_places=2, verbose_name='Стоимость')
    image = models.ImageField(upload_to='product/%Y/%m/%d', default='default/placeholder.png',  verbose_name='Картинка')

    def __str__(self):
        return f'{self.product_name} \n {self.price}'
