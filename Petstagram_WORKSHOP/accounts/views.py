from django.contrib.auth import forms as auth_forms
from django.contrib.auth import views as auth_views
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from common.view_mixins import RedirectToDashboard


# Create your views here.
class UserRegisterView(RedirectToDashboard,views.CreateView):
    template_name = 'accounts/register.html'
    form_class = auth_forms.UserCreationForm


class UserLoginView(auth_views.LoginView):
    template_name = 'accounts/login_page.html'
    success_url = reverse_lazy('dashboard')


class UserProfileView(auth_views.TemplateView):
    template_name = 'accounts/profile.html'


class EditUserProfileView(views.UpdateView):
    template_name = 'accounts/edit_profile.html'
    form_class = auth_forms.UserChangeForm


class EditPasswordView(auth_views.PasswordChangeView):
    template_name = 'accounts/edit_password.html'


from django.shortcuts import render

# Create your views here.
