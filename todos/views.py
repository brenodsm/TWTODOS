from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Todo
from django.urls import reverse_lazy


    
class TodoListView(ListView):#cbv
    model = Todo #informando com qual modelo a classe ira trabalhar
    

class TodoCreateView(CreateView): #quando usamos o Create é obrigatorio usar o field
    model = Todo
    fields = ["title", "deadline"]
    success_url = reverse_lazy("todo_list")
    