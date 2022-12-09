from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from core import settings
from manufacturing.views.products import HomePageView
from core.base_view import base_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('manufacturing.urls')),
    path('', HomePageView.as_view(), name='home'),
    path('search', base_view, name='search')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
