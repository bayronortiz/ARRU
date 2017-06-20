from django.conf.urls import url
from . import views

app_name = "estudiante"
urlpatterns = [
    url(r'^index$', views.index, name='index'),
    url(r'^registro$', views.RegistrarEstudiante.as_view(), name='registro_estudiante' ),
    url(r'^reserva$', views.ReservarRuta.as_view(), name='reserva_ruta' ),
    url(r'^cancelar$', views.eliminar_ruta, name='cancelar_ruta'),
    url(r'^informacion$',views.informacion,name='informacion'),
]