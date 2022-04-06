from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return f'@{self.usuario}'

class Mascota(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    mascota = models.CharField(max_length=60)
    sexo = models.CharField(max_length=1)
    especie = models.CharField(max_length=60)

    def __str__(self):
        return f'Mascota {self.mascota} {self.perfil.usuario}'


class Cita(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    fecha = models.DateTimeField()

    def __str__(self):
        return f'Cita de {self.mascota.mascota} {self.perfil.usuario}'
