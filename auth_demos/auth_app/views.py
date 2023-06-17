from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import views as auth_views, login
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView,ListView

from auth_app.forms import UserRegistrationForm
from auth_app.models import Profile


# Create your views here.
class UserRegistrationView(CreateView):
    template_name = 'auth/register.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result

class UserLoginView(auth_views.LoginView):
    template_name = 'auth/login.html'

    success_url = reverse_lazy('index')
class UserLogOutView(auth_views.LogoutView):
    template_name = 'index.html'

