from django.urls import path

from accounts import views
from accounts.views import *

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login user'),
    #profile
    path('profile/<int:pk>',ShowProfileView.as_view(),name='profile'),
    path('profile/create/',UserRegisterView.as_view(),name='create_profile'),
    path('profile/edit/<int:pk>', EditUserProfileView.as_view(), name='edit_profile'),
    #path('profile/delete/', delete_profile, name='delete_profile'),
]