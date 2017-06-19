from django.conf.urls import url
from django.contrib import admin
from . import views
from django.contrib.auth.views import login

app_name = "administrador"
urlpatterns = [
    url(r'^$', views.index, name='index'),   
    url(r'^login/$', login, { 'template_name':'administrador/login.html'}),   
]