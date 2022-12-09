from manufacturing.views.products import HomePageView, ProductUpdateView, ProductDetailView, ProductCreateView, \
    product_delete
from django.urls import path

urlpatterns = [
    path('new', ProductCreateView.as_view(), name='new_product'),
    path('update/<pk>', ProductUpdateView.as_view(), name='product_update'),
    path('delete/<pk>', product_delete, name='delete_product'),
    path('<pk>', ProductDetailView.as_view(), name='product_detail'),
]
