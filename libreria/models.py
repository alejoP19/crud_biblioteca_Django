from django.db import models
import os






class Libro(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100, verbose_name='Título')
    imagen = models.ImageField(upload_to='libros/', null=True, verbose_name='Imagen')
    descripcion = models.TextField(null=True, verbose_name='Descripción')

    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    

    def __str__(self):
        fila = 'titulo' + self.titulo + " " +  'descripcion' + self.descripcion
      
        return fila

# sentencia para eliminar la imagen de la carpeta media/libros 
# al eliminar el registro de  un libro

    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()
