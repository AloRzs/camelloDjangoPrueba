from django.contrib import admin

from .models import(
    Usuario,
    Venta,
    DetalleVenta,
    RegistroVenta,
    Combo
)

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Venta)
admin.site.register(DetalleVenta)
admin.site.register(RegistroVenta)
admin.site.register(Combo)