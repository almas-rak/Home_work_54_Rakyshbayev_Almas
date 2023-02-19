from django import forms
from my_market.models import Product


class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('product_name', 'description', 'price', 'category', 'image')
