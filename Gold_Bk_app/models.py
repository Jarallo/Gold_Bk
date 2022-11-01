from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Usuario(AbstractUser):
    direccion = models.CharField(max_length=80,null=True)
    telefono = models.CharField(max_length=20,null=True)
    fecha_nacimiento = models.DateField(auto_now=True, null=True)
    token = models.CharField(max_length=100, default='', null=True, blank=True)

class Activo(models.Model):
    nombre_activo = models.CharField(max_length=50)
    precio_activo = models.FloatField()
    precio_H = models.FloatField()
    precio_L = models.FloatField()
    precio_O = models.FloatField()
    precio_C = models.FloatField()

class Cuenta(models.Model):
    id_usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    capital = models.FloatField()
    ganacias = models.FloatField()



class Trade(models.Model):
    id_cuenta = models.ForeignKey(Cuenta, on_delete=models.PROTECT)
    id_activo = models.ForeignKey(Activo, on_delete=models.PROTECT)
    tipo_trade = models.CharField(max_length=5)
    precio_entrada = models.FloatField()
    precio_salida = models.FloatField()
    stoploss = models.FloatField()
    target = models.FloatField()
    profit = models.FloatField()