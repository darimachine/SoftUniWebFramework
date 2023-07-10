from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView

from web_test.models import Profile


# Create your views here.


class ProfileCreateView(CreateView):
    model = Profile
    fields = '__all__'
    template_name = 'profile/create.html'

    def get_success_url(self):
        return reverse_lazy('profile details', kwargs={'pk': self.object.pk})


class ProfileListView(ListView):
    model = Profile
    template_name = 'profile/list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['user'] = self.request.user.username
        else:
            context['user'] = 'No User'
        return context


class ProfileDetailsView(DetailView):
    model = Profile
    template_name = 'profile/details.html'
