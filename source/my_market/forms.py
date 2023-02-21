from django import forms
from my_market.models import Product, Category


class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('product_name', 'description', 'price', 'category', 'image')


class AddProductCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('category_name', 'description')

