from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

from my_market.models import Product


def index_view(request: WSGIRequest):
    products = Product.objects.all()
    return render(request, 'index.html', context={'products': products})
