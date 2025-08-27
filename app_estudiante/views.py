from django.shortcuts import render, redirect, get_object_or_404
from .models import Estudiante
# Create your views here.

def listar_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'listar_estudiantes.html', {'estudiantes': estudiantes})

def agregar_estudiante(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        telefono = request.POST['telefono']
        
        Estudiante.objects.create(
            nombre=nombre, 
            telefono=telefono
        )
        return redirect('inicio')
    return render(request, 'agregar_estudiante.html')

def editar_estudiante(request, id):
    estudiante = get_object_or_404(Estudiante, id=id)
    
    if request.method == 'POST':
        estudiante.nombre = request.POST['nombre']
        estudiante.telefono = request.POST['telefono']
        estudiante.save()
        return redirect('inicio')
    
    return render(request, 'editar_estudiante.html', {'estudiante': estudiante})

def borrar_estudiante(request, id):
    estudiante = get_object_or_404(Estudiante, id=id)
    
    if request.method == 'POST':
        estudiante.delete()
        return redirect('inicio')
    
    return render(request, 'borrar_estudiante.html', {'estudiante': estudiante})