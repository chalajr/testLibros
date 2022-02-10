from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField("Titulo",max_length=50)
    description = models.TextField("Descripcion",max_length=500)
    autor = models.CharField("Autor",max_length=50)

    def __str__(self):
        return self.title