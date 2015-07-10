from django.db import models
from django.contrib import admin
from tinymce import models as tinymce_models
from PIL import Image
from django.contrib.auth.models import User

ESTADO_VISIBLE = [1,2]

class Post(models.Model):
    title = models.CharField(max_length = 140)
    body = models.TextField()
    date = models.DateTimeField()
    #image = models.ImageField()

    def __unicode__(self):
        return self.title

class Categorias(models.Model):
    name = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    slug = models.SlugField(max_length=50, unique=True, help_text='Esto es para la URL.')
    descripcion = models.TextField()
    creada_en = models.DateTimeField(auto_now_add=True)
    actualizada_al = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'categorias'
        ordering = ['-creada_en']
        verbose_name_plural = 'Categorias'
    def __unicode__(self):
        return self.nombre 

