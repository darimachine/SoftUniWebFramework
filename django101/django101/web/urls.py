from django.urls import path

from django101.web.views import *

urlpatterns=[
    path('',TodosListList.as_view(),name='index'),
    path('todo/<int:pk>/',TodoDetailView.as_view(),name='detail'),
    path('create/',TodoCreateView.as_view(),name='create'),
]