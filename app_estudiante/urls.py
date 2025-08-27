from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_estudiantes, name='inicio'),
    path('agregar/', views.agregar_estudiante, name='agregar_estudiante'),
    path('editar/<int:id>/', views.editar_estudiante, name='editar_estudiante'),
    path('borrar/<int:id>/', views.borrar_estudiante, name='borrar_estudiante'),
]