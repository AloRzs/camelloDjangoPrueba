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
    path('login/', views.login, name='login'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout_view, name='logout'),

#path de el carrito compra ojala vaya bien diosito
    path('detalle/<int:producto_id>',views.detalle, name='detalle'),
    path('carrito/',views.carrito, name='carrito'),
<<<<<<< Updated upstream
    path('vaciar_carro/',views.vaciar_carro, name='vaciar_carro'),
=======
>>>>>>> Stashed changes
]