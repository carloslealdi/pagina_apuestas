from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Usuario(models.Model):

    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    departamento = models.CharField(max_length=100)
    municipio = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    tipo_doc = models.CharField(max_length=100)
    n_doc = models.CharField(max_length=100)
    n_cel = models.CharField(max_length=100)
    fecha_creacion = models.DateField()

    class Meta:
        db_table = 'usuario'
