from django.db import models
from django.db.models import CASCADE

#Arturo
class Autor(models.Model):
    autor = models.CharField("Autor", max_length=100)
    archivo = models.FileField(upload_to='uploads/files/archivos')
    def __str__(self):
        return self.autor

#Dennis
class Editorial(models.Model):
        nombre = models.CharField("Nombre",max_length=50)
        imagen = models.ImageField(upload_to='uploads/editoriales/imagenes')

        def __str__(self):
            return self.nombre

class Book(models.Model):
    title = models.CharField("Titulo",max_length=50)
    description = models.TextField("Descripcion",max_length=500)
    # autor = models.ForeignKey(Autor, on_delete=CASCADE)
    # editorial = models.ForeignKey(Editorial, on_delete=CASCADE)

    def __str__(self):
        return self.title