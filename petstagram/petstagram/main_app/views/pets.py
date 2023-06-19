from django.views import generic as views
from django.shortcuts import render, redirect

from ..forms import CreatePetForm, DeletePetForm
from ..helpers import get_profile
from ..models import PetPhoto, Pet

class CreatePetView(views.CreateView):
    model = Pet
    form_class = CreatePetForm
def create_pet(request):
    if request.method == "POST":
        pet_form = CreatePetForm(request.POST,instance=Pet(user_profile=get_profile()))
        if pet_form.is_valid():
            pet_form.save()
            return redirect('profile')
    else:
        pet_form = CreatePetForm()

    context={
        'pet_form':pet_form,
    }
    return render(request,'pet_create.html',context)

def edit_pet(request,pk):
    pet = Pet.objects.get(pk=pk)
    if request.method == "POST":
        pet_form = CreatePetForm(request.POST, instance=pet)
        if pet_form.is_valid():
            pet_form.save()
            return redirect('profile')
    else:
        pet_form = CreatePetForm(instance=pet)

    context = {
        'pet_form': pet_form,
        'pet':pet,
    }
    return render(request, 'pet_edit.html', context)


def delete_pet(request,pk):
    pet = Pet.objects.get(pk=pk)
    if request.method == "POST":
        pet_form = DeletePetForm(request.POST, instance=pet)
        if pet_form.is_valid():
            pet_form.save()
            return redirect('profile')
    else:
        pet_form = DeletePetForm(instance=pet)

    context = {
        'pet_form': pet_form,
        'pet': pet,
    }

    return render(request,'pet_delete.html',context)