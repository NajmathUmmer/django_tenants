from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView
from django.views import View
from .models import Task
from customers.models import Client,Domain

# Create your views here.
class Home(ListView):
    model = Task
    template_name = 'base.html'