from django.conf.urls import url
from django.urls import path, include

from . import views





urlpatterns= [
    path('index/',views.index,name='index'),
    path('lista_productos/',views.lista_productos, name='lista_productos'),
    path('contacto/',views.contacto, name='contacto'),
    path('nosotros/',views.nosotros, name='nosotros'),
    path('ers/',views.ers, name='ers'),
    path('compra/',views.compra, name='compra'),
#path de la func login
    path('mostrar_registro/', views.mostrar_registro, name='mostrar_registro'),
    path('mostrar_entrar/', views.mostrar_entrar, name='mostrar_entrar'),
    path('cerrar_sesion/', views.cerrar_sesion, name='cerrar_sesion'),
#path de el carrito compra ojala vaya bien diosito
    path('detalle/<int:producto_id>',views.detalle, name='detalle'),
    path('carrito/',views.carrito, name='carrito'),
    path('vaciar_carro/',views.vaciar_carro, name='vaciar_carro'),
#path para el crud de productos
    path('agregar_producto_crud/',views.agregar_producto_crud,name='agregar_producto_crud'),
    path('mostrar_productos_crud/',views.mostrar_producto_crud,name='mostrar_productos_crud'),
    path('modificar_crud/<int:producto_id>',views.modificar_crud,name='modificar_crud'),
    path('eliminar_crud/<int:producto_id>',views.eliminar_combo,name='eliminar_crud'),
]