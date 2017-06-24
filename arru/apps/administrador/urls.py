from django.conf.urls import url
from . import views
from django.contrib.auth.views import login

app_name = "administrador"
urlpatterns = [
    url(r'^$', login, {'template_name':'administrador/login.html'}, name='login'),
    url(r'^index/$', views.index, name='index'),
]