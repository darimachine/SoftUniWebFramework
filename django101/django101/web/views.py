from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import *

from django101.web.models import Todo


# Create your views here.
@login_required
def index(request):
    context = {
        'title': 'Django101'
    }
    print(authenticate(request,username="serhan", password="123456"))
    return render(request, 'index.html', context)


class PetView(View):

    def get(self, request):
        context = {
            'title': 'Django101-view'
        }
        return render(request, 'index.html', context)


class IndexTemplateView(TemplateView):
    template_name = 'index.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Django101-template'
        return context


class TodosListList(ListView):
    model = Todo
    template_name = 'todos_list.html'
    context_object_name = 'todo_list'

    def get_context_data(self, *, object_list=None, **kwargs):

        context = super().get_context_data(**kwargs)
        context['title'] = 'Django101-list'
        return context

    def get_queryset(self):
        queryset = super().get_queryset()


        return queryset


class TodoDetailView(DetailView):
    model = Todo
    template_name = 'todo_detail.html'
    context_object_name = 'todo'

class TodoCreateView(CreateView):
    model = Todo
    fields = '__all__'
    template_name = 'create_todo.html'
    success_url = reverse_lazy('index')
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['title'].label='aaaaaaTitle'
        return form

    def get_form_class(self):
        return super().get_form_class()



