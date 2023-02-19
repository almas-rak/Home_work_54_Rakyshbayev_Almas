from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from my_market.views.base import index_view
from my_market.views.test_views import image_upload_view

urlpatterns = [
    path('', index_view),
    path('upload/', image_upload_view),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
print(urlpatterns)