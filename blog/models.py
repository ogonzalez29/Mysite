from django.db import models


class Post(models.Model):
    title = models.CharField(max_length = 140)
    body = models.TextField()
    date = models.DateTimeField()
    #image = models.ImageField()

    def __unicode__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(
        max_length=50
        )
    amount = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        default=0
        )
