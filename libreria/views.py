from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Libro
from .forms import LibroForm

  
def  inicio(request):

    return render(request,  'paginas/inicio.html')

def  created_books(request):
    created_books=(Libro.objects.all())
    return render(request,  'libros/index.html',{"datos_libro": created_books})

def crear_libro(request):
        # request.FILES or None --> sirve para recibir lo archivos o datos que se han mostradoe n el formulario.
        formulario = LibroForm(request.POST or None,request.FILES or None)
        if formulario.is_valid():
            formulario.save()
            return redirect('Libros')
         
        return render(request, 'libros/crear.html',{'formulario':formulario})

def  editar_libro(request ,id):
     libro =Libro.objects.get(id=id)
     formulario = LibroForm(request.POST or None,request.FILES or None, instance=libro)
     if formulario.is_valid() and request.method == 'POST':
            formulario.save()
            return redirect('Libros')
     return render(request, 'libros/editar.html',{'formulario':formulario})

def  eliminar_libro(request, id):
    libro =Libro.objects.get(id=id)
    libro.delete()
    return redirect('Libros')
         



def  nosotros(request):
    return render(request, 'paginas/nosotros.html')
  
def  base(request):
    return render(request, 'base.html')

    
