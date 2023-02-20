from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect
from my_market.forms import AddProductForm


# Create your views here.


def add_product_view(request: WSGIRequest):
    if request.method == 'GET':
        form = AddProductForm()
        return render(request, 'add_product.html', context={'form': form})
    else:
        form = AddProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
