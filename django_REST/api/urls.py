

from django.urls import path

from api.views import *

urlpatterns = [
    path('manualproducts',ManualProductListView.as_view(),name='product-list'),
    path('products',ProductsListView.as_view(),name='product-list'),
    path('createproducts',ProductsCreateView.as_view(),name='product-list'),
    path('products/<int:pk>',SinglePdocutView.as_view(),name='product-detail'),
    path('categories',CategoryListView.as_view(),name='category-list'),
]