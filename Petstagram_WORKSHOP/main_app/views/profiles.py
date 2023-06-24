from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import DetailView, CreateView

from ..forms import CreateProfileForm, EditProfileForm, DeleteProfileForm
from ..helpers import get_profile
from ..models import PetPhoto, Pet, Profile


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

class ShowProfileView(DetailView):
    model = Profile
    template_name = 'profile_details.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pets = list(Pet.objects.filter(user_id=self.object.user_id))
        pet_photos = PetPhoto.objects.filter(tagged_pets__in=pets).distinct()
        total_likes_count = sum(pp.likes for pp in pet_photos)
        total_pet_photos_count = len(pet_photos)
        context['total_likes_count'] = total_likes_count
        context['total_images_count'] = total_pet_photos_count
        context['pets'] = pets
        context['is_owner'] = self.object.user_id == self.request.user.id
        return context


class CreateProfileView(CreateView):
    model = Profile
    template_name = 'profile_create.html'
    form_class = CreateProfileForm
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')
        return super().dispatch(request, *args, **kwargs)
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