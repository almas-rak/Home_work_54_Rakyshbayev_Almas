from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect
from my_market.forms import AddProductCategoryForm


def add_category_product(request: WSGIRequest):
    if request.method == 'GET':
        form = AddProductCategoryForm()
        return render(request, 'add_product.html', context={'form': form})
    else:
        form = AddProductCategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
