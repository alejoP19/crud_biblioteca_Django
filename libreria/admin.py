from django.contrib import admin
from django.db import models
from .models import Libro
# Register your models here.




class LibroAdmin(admin.ModelAdmin):
    list_display=('titulo', 'imagen','descripcion')
    search_fields=('titulo', 'imagen','descripcion')
    readonly_fields=('created','updated')


admin.site.register(Libro,LibroAdmin)

