from django.db import models
from django.utils import timezone

class Postear(models.Model):
    Autor = models.ForeignKey('auth.User')
    Titulo = models.CharField(max_length=200)
    Texto = models.TextField()
    Fecha_de_Creacion = models.DateTimeField(default=timezone.now)
    Fecha_de_Publicacion = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.Fecha_de_Publicacion = timezone.now()
        self.save()

    def __str__(self):
        return self.Titulo

# Create your models here.
