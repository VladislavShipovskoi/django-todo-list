from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .models import Todo


def todo_detail(request, pk):
    todos = get_object_or_404(Todo, pk=pk)
    return render(request, 'todolist/todo_detail.html', {'todos': todos})

def index(request):
    return render(request, 'todolist/base.html')


def todo_list(request):
    todos = Todo.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'todolist/todo_list.html', {'todos': todos})
