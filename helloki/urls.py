from django.urls import path
from .views import HelloViewki
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', HelloViewki.as_view(), name='indexki'),
    path('index1', HelloViewki.as_view(), name='index1'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)