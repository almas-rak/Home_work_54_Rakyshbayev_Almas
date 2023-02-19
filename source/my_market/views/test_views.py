from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect

from my_market.forms import ImageForm


# Create your views here.


def image_upload_view(request: WSGIRequest):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            return redirect(request, 'index.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'test.html', {'form': form})
