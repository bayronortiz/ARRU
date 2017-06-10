from django.conf.urls import url
from django.contrib import admin
from . import views

app_name = "estudiante"
urlpatterns = [
    #url(r'^$', views.index, name='index')
    #url(r'^$', views.IndexView.as_view(), name='index' ),
    url(r'^registro$', views.RegistrarEstudiante.as_view(), name='registro_estudiante' ),
    url(r'^reserva$', views.ReservarRuta.as_view(), name='reserva_ruta' ),
    url(r'^cancelar/(?P<pk>\d+)/$', views.CancelarRuta.as_view(), name='cancelar_ruta' ),
]