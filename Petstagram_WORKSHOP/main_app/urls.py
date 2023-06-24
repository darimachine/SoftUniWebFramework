from django.urls import path

from .views.generic import  ShowDashboardView, show_error, HomeView
from .views.pet_photos import *
from .views.pets import *
from .views.profiles import *

urlpatterns = [
    path('',HomeView.as_view(),name='index'),
    path('dashboard/',ShowDashboardView.as_view(),name='dashboard'),
    #profile
    path('profile/<int:pk>',ShowProfileView.as_view(),name='profile'),
    path('profile/create/',create_profile,name='create_profile'),
    path('profile/edit/', edit_profile, name='edit_profile'),
    path('profile/delete/', delete_profile, name='delete_profile'),
    #pet
    path('pet/create', CreatePetView.as_view(), name='create_pet'),
    path('pet/edit/<int:pk>/', EditPetView.as_view(), name='edit_pet'),
    path('pet/delete/<int:pk>/', DeletePetView.as_view(), name='delete_pet'),
    #PetPhoto
    path('photo/details/<int:pk>', ShowPetPhotoDetail.as_view(), name='pet_photo_details'),
    path('photo/like/<int:pk>/', like_pet, name='like_pet_photo'),
    path('photo/add/', CreatePetPhotoView.as_view(), name='pet_photo_create'),
    path('photo/edit/<int:pk>/', edit_pet_photo, name='pet_photo_edit'),
    #error
    path('error_401/', show_error, name='401_error'),


]