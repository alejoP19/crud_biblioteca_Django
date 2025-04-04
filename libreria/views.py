from django.shortcuts import render

from .models import Libro
from .forms import LibroForm





def  nosotros(request):
    return render(request, 'paginas/nosotros.html')
  
def  base(request):
    return render(request, 'base.html')
def  inicio(request):

    return render(request,  'paginas/inicio.html')


  
def  crear_libro(request):
        formulario = LibroForm(request.POST or None)
        return render(request, 'libros/crear.html',{'formulario ':formulario})

def  editar_libro(request):
    return render(request, 'libros/editar.html')

def  eliminar_libro(request):
    return render(request, '')


def  created_books(request):
    created_books=(Libro.objects.all())
    return render(request,  'libros/index.html',{"datos_libro": created_books})


    
