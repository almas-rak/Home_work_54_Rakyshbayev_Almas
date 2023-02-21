from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, get_object_or_404, redirect

from my_market.forms import AddProductCategoryForm
from my_market.models import Category


def add_category_product(request: WSGIRequest):
    if request.method == 'POST':
        form = AddProductCategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddProductCategoryForm()
        return render(request, 'add_product_category.html', context={'form': form})


def view_categories(request: WSGIRequest):
    categories = Category.objects.all()
    return render(request, 'categories_view.html', context={'categories': categories})


def category_view(request: WSGIRequest, pk):
    category = get_object_or_404(Category, pk=pk)
    return render(request, 'detail_view_category.html', context={'category': category})


# def edit_category(request: WSGIRequest, pk):
#     if request.method == 'GET':
#         category = get_object_or_404(Category, pk=pk)
#         return render(request, 'edit_category.html', context={'category': category})



    
