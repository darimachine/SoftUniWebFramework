from django.urls import path

from accounts import views

urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='login user'),
]