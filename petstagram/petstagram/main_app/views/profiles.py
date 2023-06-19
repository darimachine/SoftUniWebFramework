from django.shortcuts import render, redirect

from ..forms import CreateProfileForm, EditProfileForm, DeleteProfileForm
from ..helpers import get_profile
from ..models import PetPhoto,Pet


def show_profile(request):
    profile = get_profile()
    pets = Pet.objects.filter(user_profile=profile)
    pet_photos = PetPhoto.objects.filter(tagged_pets__in=pets).distinct()
    total_likes_count = sum(pp.likes for pp in pet_photos)
    total_pet_photos_count = len(pet_photos)
    #------- НЕ ОПТИМИЗИРАН ВАРИАНТ
        # total_likes_count = sum(photo.likes for photo in PetPhoto.objects.filter(tagged_pets__user_profile=profile).distinct())
        # total_pet_photos_count =len(PetPhoto.objects.filter(tagged_pets__user_profile=profile).distinct())
    context = {
        'profile':profile,
        'total_likes_count': total_likes_count,
        'total_images_count':total_pet_photos_count,
        'pets':pets,
    }
    return render(request,'profile_details.html',context)

def create_profile(request):
    if request.method == 'POST':
        profile_form=CreateProfileForm(request.POST, request.FILES)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('dashboard')
    else:
        profile_form = CreateProfileForm()

    context={
        'profile_form':profile_form,
    }
    return render(request,'profile_create.html',context)

def edit_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        profile_form= EditProfileForm(request.POST, instance=profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('profile')
    else:
        profile_form = EditProfileForm(instance=profile)

    context={
        'profile_form':profile_form,
    }
    return render(request,'profile_edit.html',context)


def delete_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        profile_form = DeleteProfileForm(request.POST, instance=profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('index')
    else:
        profile_form = DeleteProfileForm(instance=profile)

    context = {
        'profile_form': profile_form,
    }
    return render(request,'profile_delete.html',context)