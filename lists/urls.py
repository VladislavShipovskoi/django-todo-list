from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    url(r'^$', login_required(views.TodoList.as_view()), name='todo_list'),
    url(r'^todo/new/$', login_required(views.TodoCreate.as_view()),
        name='todo_new'),
    url(r'^todo/completed/$', login_required(views.TodoListComplete.as_view()),
        name='todo_completed'),
    url(r'^todo/(?P<pk>\d+)/edit/$', login_required(views.TodoUpdate.as_view()),
        name='todo_edit'),
    url(r'^todo/(?P<pk>\d+)/delete/$',
        login_required(views.TodoDelete.as_view()), name='todo_delete'),
    url(r'^registration/$', views.RegistrationFormView.as_view()),
    url(r'^login/$', views.LoginFormView.as_view()),
    url(r'^auth/', include('social_django.urls', namespace='social')),
    url(r'^logout/$', views.LogoutView.as_view()),
]
