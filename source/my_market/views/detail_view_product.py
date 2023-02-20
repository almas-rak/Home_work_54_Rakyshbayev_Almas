from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, get_object_or_404

from my_market.models import Product


def detail_view_product(request: WSGIRequest, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'detail_view_product.html', context={'product': product})
