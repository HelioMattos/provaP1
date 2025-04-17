from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from .models import Prova

class ProvaListView(ListView):
    model = Prova

class ProvaCreateView(CreateView):
    model = Prova
    fields =['title', 'matricula', 'deadline']
    success_url = reverse_lazy('prova_list')
    
