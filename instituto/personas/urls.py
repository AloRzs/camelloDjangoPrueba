from django.conf.urls import url
from django.urls import path, include

from . import views





urlpatterns= [
    path('index',views.index,name='index'),
    path('lista_productos',views.lista_productos, name='lista_productos'),
    path('contacto',views.contacto, name='contacto'),
    path('nosotros',views.nosotros, name='nosotros'),
    path('ers',views.ers, name='ers'),


#path de la func login
    path('login', views.login, name='login'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout_view, name='logout'),
]