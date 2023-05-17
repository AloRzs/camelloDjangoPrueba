from django.conf.urls import url
from django.urls import path, include

from . import views





urlpatterns= [
    path('index/',views.index,name='index'),
    path('lista_productos/',views.lista_productos, name='lista_productos'),
    path('contacto/',views.contacto, name='contacto'),
    path('nosotros',views.nosotros, name='nosotros'),
    path('ers/',views.ers, name='ers'),
    path('api/',views.api, name='api'),

    #path de la func carrito
    path('cart/', views.carrito, name='cart'),
    path('cart/agregar/<int:producto_id>/', views.agregar_carrito, name='agregar_carrito'),
    path('cart/restar/<int:producto_id>/', views.sacar_del_carrito, name='sacar_del_carrito'),
    path('cart/limpiar/', views.limpiar_carrito, name='limpiar'),

    #path de la func login
    path('login/', views.login, name='login'),
    path('logout/', views.logout_view, name='logout'),
]