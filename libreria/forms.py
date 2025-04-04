
from django import forms

from .models import Libro



class LibroForm(forms.ModelForm):
        class meta:
          model = Libro
          fields = ['id','titulo','imagen','descripcion']
           
        #   fields ='__all__'
       
    