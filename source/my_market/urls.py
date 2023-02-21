from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from my_market.views.base import index_view
from my_market.views.add_view import add_product_view
from my_market.views.detail_view_product import detail_view_product
from my_market.views.add_category_product import add_category_product

urlpatterns = [
    path('', index_view, name='home'),
    path('add/product/', add_product_view, name='add_product'),
    path('add/category/', add_category_product, name='add_category'),
    path('view/product/<int:pk>', detail_view_product, name='detail_view_product')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
print(urlpatterns)
