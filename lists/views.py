from django.shortcuts import redirect
from django.utils import timezone
from .models import Todo
from .forms import TodoForm
from django.views.generic.edit import (
    FormView,
    CreateView,
    DeleteView,
    UpdateView,
)
from django.views.generic.list import ListView
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
)
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.contrib.auth import login,logout
from django.urls import reverse_lazy


class RegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = "/login/"
    template_name = "todolist/register.html"

    def form_valid(self, form):
        form.save()
        return super(
            RegisterFormView,
            self
        ).form_valid(form)


class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = "todolist/login.html"
    success_url = "/"

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(
            LoginFormView,
            self
        ).form_valid(form)


class LogoutView(View):

    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/")


class TodoCreate(CreateView):
    form_class = TodoForm
    template_name = 'todolist/todo_new_and_edit.html'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.author = self.request.user
        instance.created_date = timezone.now()
        instance.save()
        return redirect('todo_list')


class TodoDelete(DeleteView):
    model = Todo
    success_url = reverse_lazy('todo_list')


class TodoUpdate(UpdateView):
    form_class = TodoForm
    model = Todo
    template_name = 'todolist/todo_new_and_edit.html'
    success_url = '/'


class TodoList(ListView):
    model = Todo
    template_name = 'todolist/todo_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = context['object_list'].filter(
            author=self.request.user, success=False).order_by('-priority')
        return context


class TodoListComplete(ListView):
    model = Todo
    template_name = 'todolist/todo_completed.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = context['object_list'].filter(
            author=self.request.user, success=True).order_by('completed_date')
