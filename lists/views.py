from django.shortcuts import render
from django.utils import timezone
from .models import Todo


def todo_list(request):
    todos = Todo.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'todolist/todo_list.html', {'todos': todos})
