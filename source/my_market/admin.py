from django.contrib import admin
from django.utils.safestring import mark_safe

from my_market.models import Product, Category


# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'price', 'image', 'category', 'add_date_time')
    list_editable = ('product_name', 'price', 'image', 'category')
    readonly_fields = ['preview']

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="max-height: 200px;>')


admin.site.register(Product, ProductAdmin)


class CategoryProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name', 'description')
    # list_editable = ('category_name', 'description')


admin.site.register(Category, CategoryProductAdmin)
