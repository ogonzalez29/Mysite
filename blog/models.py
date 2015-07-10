from django.db import models
from django.contrib import admin
from tinymce import models as tinymce_models
from PIL import Image
from django.contrib.auth.models import User

ESTADO_VISIBLE = [1,2]

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

class ManejadorPost(models.Manager):
    def get_query_set(self):
        default_queryset = super(ManejadorPost,self).get_query_set()
        return default_queryset.filter(status__in=ESTADO_VISIBLE)

class Post(models.Model):
    # ESTADOS=((1,"Publicado"),(2,"Archivado"),(3,"Necesita Editarse"),(4,"Necesita Aprobacion"))
    # status = models.IntegerField(choices=ESTADOS,default=4)
    # objetos_panel = models.Manager()
    # objects = ManejadorPost()
    title = models.CharField(max_length = 140)
    #author = models.ForeignKey(User)
    body = models.TextField()
    date = models.DateTimeField()
    categorias_post = models.ManyToManyField(Categorias)
    #image = models.ImageField(upload_to='photos', blank = True)
    #image = models.ImageField()

    def admin_categorias(self):
        return ', '.join([a.nombre for a in self.categorias_post.all()])
    admin_categorias.short_description = "categorias"

    # class Meta:
    #     db_table = 'entradas'
    #     ordering = ['-date']
    #     verbose_name_plural = 'Posts'

    def __unicode__(self):
        return self.title



