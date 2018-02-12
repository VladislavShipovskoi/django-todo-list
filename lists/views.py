from django.shortcuts import render,redirect
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .models import Todo
from .forms import TodoForm


def todo_detail(request, pk):
    todos = get_object_or_404(Todo, pk=pk)
    return render(request, 'todolist/todo_detail.html', {'todos': todos})


def todo_new(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.author = request.user
            todo.created_date = timezone.now()
            todo.save()
            return redirect('todo_detail', pk=todo.pk)
    else:
        form = TodoForm()
    return render(request, 'todolist/todo_edit.html', {'form': form})


def todo_edit(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.author = request.user
            todo.created_date = timezone.now()
            todo.save()
            return redirect('post_detail', pk=todo.pk)
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todolist/todo_edit.html', {'form': form})


def index(request):
    return render(request, 'todolist/base.html')


def todo_list(request):
    todos = Todo.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'todolist/todo_list.html', {'todos': todos})
