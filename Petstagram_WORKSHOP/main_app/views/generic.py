from django.contrib.auth import get_user_model
from django.contrib.auth import mixins
from django.shortcuts import render, redirect
from django.views import generic as views

from ..helpers import get_profile
from ..models import PetPhoto

UserModel = get_user_model()
# def home(request):
#     context = {
#         'hide_nav_items':True,
#     }
#
#     return render(request,'home_page.html',context)
class HomeView(views.TemplateView):
    template_name = 'home_page.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hide_nav_items'] = True
        return context
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')
        return super().dispatch(request, *args, **kwargs)


class ShowDashboardView(views.ListView):
    model = PetPhoto
    template_name = 'dashboard.html'
    context_object_name = 'pet_photos'


def show_error(request):
    return render(request,'401_error.html')