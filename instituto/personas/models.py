from django.db.models import (
    Model,
    CharField,
    IntegerField,
    OneToOneField,
    ForeignKey,
    AutoField,
    DateField,
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

class Usuario(Model):
    id_usuario = AutoField(primary_key=True)
    rut = CharField(max_length=10, null=False, blank=False)
    nombre = CharField(max_length=20, null=False, blank=False)
    apellido = CharField(max_length=20, null=False, blank=False)
    contrasena = CharField(max_length=30, null=False, blank=False)
    usuario = OneToOneField(User, on_delete=CASCADE)

class Venta(Model):
    id_venta = AutoField(primary_key=True)
    fecha = DateField(auto_now=True)
    total = IntegerField(null=False, blank=False)
    producto = ManyToManyField(Combo)
    id_usuario = ForeignKey(Usuario, on_delete=CASCADE)

class DetalleVenta(Model):
    id_detalle_venta = AutoField(primary_key=True)
    id_venta = ForeignKey(Venta, on_delete=CASCADE)
    cantidad = IntegerField(null=False,blank=False)
    subtotal = IntegerField(null=False,blank=False)

class RegistroVenta(Model):
    id_regis_venta = AutoField(primary_key=True)
    id_venta = ForeignKey(Venta, on_delete=CASCADE)
