from django.shortcuts import redirect, render

from ..forms import CreatePetPhotoForm, EditPetPhotoForm
from ..helpers import get_profile
from ..models import PetPhoto


def show_pet_photo_details(request,pk):
    pet = PetPhoto.objects.get(id=pk)
    context={
        'pet_photo':pet,
    }
    return render(request,'photo_details.html',context)

def like_pet(request,pk,):
    pet_photo = PetPhoto.objects.prefetch_related('tagged_pets').get(pk=pk)
    pet_photo.likes+=1
    pet_photo.save()
    return redirect('pet_photo_details',pk)

def create_pet_photo(request):
    if request.method == "POST":
        pet_photo_form = CreatePetPhotoForm(request.POST,request.FILES)
        if pet_photo_form.is_valid():
            pet_photo_form.save()
            return redirect('dashboard')
    else:
        pet_photo_form = CreatePetPhotoForm()

    context={
        'pet_photo_form':pet_photo_form,
    }

    return render(request,'photo_create.html',context)

def edit_pet_photo(request,pk):
    pet_photo = PetPhoto.objects.get(pk=pk)
    if request.method == "POST":
        pet_photo_form = EditPetPhotoForm(request.POST, instance=pet_photo)
        if pet_photo_form.is_valid():
            pet_photo_form.save()
            return redirect('dashboard')
    else:
        pet_photo_form = EditPetPhotoForm(instance=pet_photo)

    context = {
        'pet_photo_form': pet_photo_form,
        'pet':pet_photo,
    }
    return render(request,'photo_edit.html',context)