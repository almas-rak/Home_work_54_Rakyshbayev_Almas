from django import forms
from my_market.models import Product


class ImageForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('product_name', 'price', 'image')
