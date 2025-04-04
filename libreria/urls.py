from django.urls import path
from .  import views


urlpatterns = [
 
   
    
    path('', views.inicio, name='Inicio'),
    path('nosotros/', views.nosotros, name='Nosotros'),
    path('libros/', views.created_books, name='Libros'),
    path('libros/crear/', views.crear_libro, name="CrearLibro"),
    path('libros/editar/', views.editar_libro, name="EditarLibro"),
    path('libros/eliminar/', views.eliminar_libro, name="EliminarLibro"),

]