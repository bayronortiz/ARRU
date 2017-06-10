from django.conf.urls import url
from django.contrib import admin
from . import views

app_name = "estudiante"
urlpatterns = [
    #url(r'^$', views.index, name='index')
    #url(r'^$', views.IndexView.as_view(), name='index' ),
    url(r'^registro$', views.RegistrarEstudiante.as_view(), name='registro_estudiante' ),
]