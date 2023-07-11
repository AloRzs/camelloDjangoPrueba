from django.db.models import (
    Model,
    CharField,
    IntegerField,
    OneToOneField,
    ForeignKey,
    AutoField,
    DateTimeField,
    CASCADE,
    ManyToManyField,
)
from django.contrib.auth.models import User

# Create your models here.

class Combo(Model):
    id_combo = AutoField(primary_key=True)
    precio = IntegerField(null=False,blank=False)
    stock = IntegerField(null=False,blank=False)
    foto = CharField(max_length=100,null=False,blank=False)
    descripcion = CharField(max_length=100,null=False,blank=False)

class DetalleVenta(Model):
    id_detalle_venta = AutoField(primary_key=True)
    id_combo = ForeignKey(Combo, on_delete=CASCADE)
    cantidad = IntegerField(null=False,blank=False)
    subtotal = IntegerField(null=False,blank=False)

class Venta(Model):
    id_venta = AutoField(primary_key=True)
    fecha = DateTimeField(auto_now=True)
    total = IntegerField(null=False, blank=False)
    id_detalle_venta= ForeignKey(DetalleVenta, on_delete=CASCADE)
    id_usuario = ForeignKey(User, on_delete=CASCADE)

class RegistroVenta(Model):
    id_regis_venta = AutoField(primary_key=True)
    id_venta = ForeignKey(Venta, on_delete=CASCADE)
