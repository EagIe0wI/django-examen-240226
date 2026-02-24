from django.urls import path
from . import views

urlpatterns = [
    path('', views.base_view, name='base_view'),
    path('product-list/', views.product_list, name='product_list'),
]
