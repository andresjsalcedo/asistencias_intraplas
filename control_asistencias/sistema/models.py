from django.db import models

# Create your models here.

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    rol = models.CharField(max_length=200)
    area = models.CharField(max_length=200)

    def __str__(self):
        return self.usuario