from django.urls import path
from web_test.views import *
urlpatterns=[
    path('',ProfileListView.as_view(),name='profile list'),
    path('create/',ProfileCreateView.as_view(),name='profile create'),
    path('details/<int:pk>',ProfileDetailsView.as_view(),name='profile details'),
]