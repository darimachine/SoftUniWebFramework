from django.urls import path

from .views.generic import  ShowDashboardView, show_error, HomeView
from .views.pet_photos import show_pet_photo_details, like_pet, create_pet_photo, edit_pet_photo
from .views.pets import create_pet, edit_pet, delete_pet
from .views.profiles import show_profile, create_profile, edit_profile, delete_profile

urlpatterns = [
    path('',HomeView.as_view(),name='index'),
    path('dashboard/',ShowDashboardView.as_view(),name='dashboard'),
    #profile
    path('profile/',show_profile,name='profile'),
    path('profile/create/',create_profile,name='create_profile'),
    path('profile/edit/', edit_profile, name='edit_profile'),
    path('profile/delete/', delete_profile, name='delete_profile'),
    #pet
    path('pet/create', create_pet, name='create_pet'),
    path('pet/edit/<int:pk>/', edit_pet, name='edit_pet'),
    path('pet/delete/<int:pk>/', delete_pet, name='delete_pet'),
    #PetPhoto
    path('photo/details/<int:pk>', show_pet_photo_details, name='pet_photo_details'),
    path('photo/like/<int:pk>/', like_pet, name='like_pet_photo'),
    path('photo/add/', create_pet_photo, name='pet_photo_create'),
    path('photo/edit/<int:pk>/', edit_pet_photo, name='pet_photo_edit'),
    #error
    path('error_401/', show_error, name='401_error'),


]