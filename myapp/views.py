from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView
from django.views import View
from .models import Task
from customers.models import Client,Domain
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm

# Create your views here.
class SignUp(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'signup.html'
class Home(CreateView):
    model = Task
    fields = '__all__'
    template_name = 'home.html'
class List(ListView):
    model = Task
    template_name = 'base.html'