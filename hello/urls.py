from django.urls import path
from .views import HelloView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', HelloView.as_view(), name='index'),
    path('index1', HelloView.as_view(), name='index1'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)