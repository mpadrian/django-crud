from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.core.exceptions import ValidationError


class Publicacion(models.Model):
    """
    Modelo para las publicaciones de los usuarios
    """
    # Campo de relación con el usuario
    autor = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        verbose_name="Autor"
    )
    
    # Campos principales
    titulo = models.CharField(
        max_length=200,
        verbose_name="Título",
        help_text="Escribe un título llamativo para tu publicación"
    )
    
    descripcion = models.TextField(
        verbose_name="Descripción",
        help_text="Desarrolla el contenido de tu publicación"
    )
    
    imagen = models.ImageField(
        upload_to='publicaciones/%Y/%m/%d/',
        verbose_name="Imagen destacada",
        blank=True,
        null=True,
        help_text="Sube una imagen relacionada con tu publicación"
    )
    
    # Campos automáticos
    fecha_creacion = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Fecha de creación"
    )
    
    fecha_actualizacion = models.DateTimeField(
        auto_now=True,
        verbose_name="Última actualización"
    )
    
    # Metadata
    class Meta:
        verbose_name = "Publicación"
        verbose_name_plural = "Publicaciones"
        ordering = ['-fecha_creacion']
    
    def __str__(self):
        return f"{self.titulo} - {self.autor.username}"