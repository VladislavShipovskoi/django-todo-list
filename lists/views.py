from django.shortcuts import redirect
from django.contrib import messages
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
from django.contrib.auth import login
from django.contrib.auth.views import logout
from django.urls import reverse_lazy


REGISTRATION_SUCCESSFUL = "Registration successfully"
LOGIN_SUCCESSFUL = "Logged in successfully"
LOGOUT_SUCCESSFUL = "Logged out successfully"
INVALID_USER_OR_PASSWORD = "Username or Password invalid. Please try again"


class RegistrationFormView(FormView):
    form_class = UserCreationForm
    success_url = "/login/"
    template_name = "todolist/registration.html"

    def form_valid(self, form):
        form.save()
        messages.add_message(
            self.request,
            messages.SUCCESS,
            REGISTRATION_SUCCESSFUL
        )
        return super(
            RegistrationFormView,
            self
        ).form_valid(form)


class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = "todolist/login.html"
    success_url = "/"

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        messages.add_message(
            self.request,
            messages.SUCCESS,
            LOGIN_SUCCESSFUL
        )

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
