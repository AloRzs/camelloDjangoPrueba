from django.shortcuts import render

# Create your views here.
class Persona:
    rut=""
    nombre=""
    edad=0

    def __init__(self,rut,nombre,edad):
        self.rut=rut
        self.nombre=nombre
        self.edad=edad
    def __str__(self):
        return self.rut + ", "+ self.nombre +", "+str(self.edad)
#esto para crear los productos, lo iremos adaptando segun nuestros requerimientos de pagina 



class Producto:
    id=""
    nombre=""
    precio=0
    stock=0
    foto=""     #ejemplo de foto
    descripcion=""
    def __init__(self,id,nombre,precio,stock,foto,descripcion):
        self.id=id             
        self.nombre=nombre
        self.precio=precio
        self.stock=stock
        self.foto=foto
        self.descripcion=descripcion
    def __str__(self) -> str:#implementar lo de a descripcion
        return self.id + ", "+self.nombre + ", "+self.precio+ ", "+self.stock+ ", "+self.foto+ ", " +self.descripcion






def index(request):
    print("hola estoy en index...")
    context ={}
    return render(request,'html/index.html',context)