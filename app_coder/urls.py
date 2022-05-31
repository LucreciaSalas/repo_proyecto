from django.urls import path
from . import views

urlpatterns = [

  #  path("", views.inicio), # ver porque estaba desde familiares #
    path("lista_pacientes", views.lista_pacientes),
    path("lista_prestadores", views.lista_prestadores),
    path("lista_proveedores", views.lista_proveedores),
    path("alta_pacientes", views.alta_pacientes)
]
