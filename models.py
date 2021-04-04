from django.db import models

# Create your models here.
class Diario(models.Model):
    sentimiento = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha = models.DateField()
    imagen = models.ImageField(upload_to = 'img')
    captura = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.fecha) + ' ' + self.sentimiento

