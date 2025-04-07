from django.urls import path
from .  import views


urlpatterns = [
 
   
    
    path('', views.inicio, name='Inicio'),
    path('libros/', views.created_books, name='Libros'),
    path('libros/crear/', views.crear_libro, name="CrearLibro"),
    path('libros/editar/<int:id>', views.editar_libro, name="EditarLibro"),
    path('eliminar/<int:id>', views.eliminar_libro, name="EliminarLibro"),
    path('nosotros/', views.nosotros, name='Nosotros'),

]