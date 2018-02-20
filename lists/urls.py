from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^$', views.todo_list, name='todo_list'),
    url(r'^todo/new/$', views.todo_new, name='todo_new'),
    url(r'^todo/completed/$', views.todo_completed, name='todo_completed'),
    url(r'^todo/(?P<pk>\d+)/edit/$', views.todo_edit, name='todo_edit'),
    url(r'^todo/(?P<pk>\d+)/delete/$', views.todo_delete, name='todo_delete'),
    url(r'^register/$', views.RegisterFormView.as_view()),
    url(r'^login/$', views.LoginFormView.as_view()),
    url(r'^auth/', include('social_django.urls', namespace='social')),
    url(r'^logout/$', views.LogoutView.as_view()),
]
