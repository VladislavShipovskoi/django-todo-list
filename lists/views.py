from django.shortcuts import render,redirect,get_object_or_404
from django.utils import timezone
from .models import Todo
from .forms import TodoForm
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


class RegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = "/login/"
    template_name = "todolist/register.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)


class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = "todolist/login.html"
    success_url = "/"

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/")


@login_required
def todo_new(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.author = request.user
            todo.created_date = timezone.now()
            todo.save()
            return redirect('todo_list')
    else:
        form = TodoForm()
    return render(request, 'todolist/todo_new_and_edit.html', {'form': form})


@login_required
def todo_delete(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.delete()
    return redirect('todo_list')


@login_required
def todo_edit(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.author = request.user
            todo.success = 'success' in request.POST
            todo.created_date = timezone.now()
            todo.save()
            return redirect('todo_list')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todolist/todo_new_and_edit.html', {'form': form})


@login_required
def todo_list(request):
    todos = Todo.objects.filter(author=request.user,success=False).order_by('-priority')
    return render(request, 'todolist/todo_list.html', {'todos': todos})


@login_required
def todo_completed(request):
    todos = Todo.objects.filter(author=request.user,success=True).order_by('completed_date')
    return render(request, 'todolist/todo_completed.html', {'todos': todos})
