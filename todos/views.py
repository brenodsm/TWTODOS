from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from .models import Todo
from django.urls import reverse_lazy #verificar
from django.shortcuts import  get_object_or_404, redirect
from datetime import date


    
class TodoListView(ListView):#cbv
    model = Todo #informando com qual modelo a classe ira trabalhar
    

class TodoCreateView(CreateView): #quando usamos o Create é obrigatorio usar o field
    model = Todo
    fields = ["title", "deadline"]
    success_url = reverse_lazy("todo_list")
    

class TodoUpdateView(UpdateView):  # Atualização de um item existente
    model = Todo
    fields = ["title", "deadline"]
    success_url = reverse_lazy("todo_list")
    
class TodoDeleteView(DeleteView):
    model = Todo
    success_url = reverse_lazy("todo_list")
    

class TodoCompleteView(View):
    def get(self, request, pk):
        todo = get_object_or_404(Todo, pk=pk)
        todo.finished_at = date.today()
        todo.save()
        return redirect("todo_list")
