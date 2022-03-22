from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de edición" )
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición" )

    class Meta:
        verbose_name = "categoría"
        verbose_name_plural = "categorías"
        ordering = ['-created']

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="titulo")
    content = RichTextField(verbose_name="contenido")
    published =models.DateTimeField(verbose_name="Fecha de publicacion", default=now)
    image = models.ImageField(verbose_name="Imagen", upload_to='blog', null=True, blank=True)
    # al tener entradas relacionadas, se tiene que definir accion al eliminar
    author = models.ForeignKey(User, verbose_name='Autor', on_delete=models.CASCADE)
    # related_name= define un nombre a la relacion entre 2 modelos
    categories = models.ManyToManyField(Category, verbose_name="Categorias", related_name='get_posts')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de edición" )
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición" )

    class Meta:
        verbose_name = "entrada"
        verbose_name_plural = "entradas"
        ordering = ['-created']

    def __str__(self):
        return self.title