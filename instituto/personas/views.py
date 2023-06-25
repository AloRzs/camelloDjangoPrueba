from django.shortcuts import render, redirect
from django.contrib.auth import logout

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

class Carrito:
    id=0
    precio=0
    stock=0
    foto=""     #ejemplo de foto
    descripcion=""
    cantidad=0 #esto es lo nuevo en el carrito
    def __init__(self,id,precio,stock,foto,descripcion,cantidad):
<<<<<<< Updated upstream
=======
        self.id=id             
        self.precio=precio
        self.stock=stock
        self.foto=foto
        self.descripcion=descripcion
        self.cantidad=cantidad
    def __str__(self):#implementar lo de a descripcion
        return self.id + ", "+self.precio+ ", "+self.stock+ ", "+self.foto+ ", " +self.descripcion+", " + self.cantidad

class Producto:
    id=0
    precio=0
    stock=0
    foto=""     #ejemplo de foto
    descripcion=""
    def __init__(self,id,precio,stock,foto,descripcion):
>>>>>>> Stashed changes
        self.id=id             
        self.precio=precio
        self.stock=stock
        self.foto=foto
        self.descripcion=descripcion
<<<<<<< Updated upstream
        self.cantidad=cantidad
    def __str__(self):
        str(self.id) + ", " +str(self.precio) + ", " +str(self.stock) + ", " +self.foto + ", " +self.descripcion + ", " +str(self.cantidad)

class Producto:
    id=0
    precio=0
    stock=0
    foto=""     #ejemplo de foto
    descripcion=""
    def __init__(self,id,precio,stock,foto,descripcion):
        self.id=id             
        self.precio=precio
        self.stock=stock
        self.foto=foto
        self.descripcion=descripcion
    def __str__(self):
        str(self.id) + ", " +str(self.precio) + ", " +str(self.stock) + ", " +self.foto + ", " +self.descripcion

prod1 = Producto(1,2000,45,"completo+bebida.jpg","completo con bebida")
prod2 = Producto(2,3600,54,"2completo+bebida.jpg","2 completo_+_bebida")## arreglar los espacios de la descripcion
=======
    def __str__(self):#implementar lo de a descripcion
        return self.id + ", "+self.precio+ ", "+self.stock+ ", "+self.foto+ ", " +self.descripcion

prod1 = Producto(1,2000,45,"completo+bebida.jpg","completo + bebida")
prod2 = Producto(2,3600,54,"2completo+bebida.jpg","2 completo + bebida")
>>>>>>> Stashed changes
prod3 = Producto(3,2000,70,"salchipapa +bebida.jpg","salchipapa + bebida")
prod4 = Producto(4,5600,42,"chorrillana familiar+bebida.jpg","chorrillana familiar + bebida")
prod5 = Producto(5,4500,56,"chorrillana+bebida.jpg","chorrillana + bebida")
prod6 = Producto(6,8400,46,"chorrillana familiar+bebida.jpg","familiar + bebida")
prod7 = Producto(7,4800,67,"churrasco+bebida.jpg","churrasco + bebida")
prod8 = Producto(8,9000,82,"2 churrascos+bebida.jpg","2 churrascos + bebida")
prod9 = Producto(9,16500,52,"4 churrascos+bebida.jpg","4 churrascos + bebida")
prod10 = Producto(9,2500,33,"hamburguesa queso+bebida.jpg","hamburguesa queso + bebida")
prod11 = Producto(11,8500,35,"4 hamburguesa queso + bebida.jpg","4 hamburguesa queso + bebida")
prod12 = Producto(12,20000,30,"4 italianos + 2 bebidas individuales.jpg","4 italianos + 2 bebidas individuales")
prod13 = Producto(13,4800,31,"2 salchipapas individual + bebida 1 lt.jpg","2 salchipapas individual + bebida 1 lt")
prod14 = Producto(14,9000,36,"pizza individual + bebida individual.jpg","pizza individual + bebida individual")
prod15 = Producto(15,16500,33,"pizza familiar + bebida 1 lt.jpg","pizza familiar + bebida 1 lt")
prod16 = Producto(16,4800,54,"2 pizza familiar + bebida 3 lt.jpg","2 pizza familiar + bebida 3 lt")
prod17 = Producto(17,9000,60,"2 pizza individual + 2 bebida individual.jpg","2 pizza individual + 2 bebida individual")
prod18 = Producto(18,16500,43,"pizza individual + 4 empanadas + bebida individual.jpg","pizza individual + 4 empanadas + bebida individual")
prod19 = Producto(19,4800,55,"pizza familiar + 16 empanadas + bebida 3 lt.jpg","pizza familiar + 16 empanadas + bebida 3 lt")
prod20 = Producto(20,20000,56,"Big camello.png","2 completos italianos+ 2 churrascos italiano + bebida 3 lt.")

listaCarrito=[]

listaProductosMain=[prod1,prod2,prod3,prod4,prod5,prod6,prod7,prod8,prod9,prod10,prod11,prod12,prod13,prod14,prod15
                ,prod16,prod17,prod18,prod19,prod20]

def index(request):
    print("hola estoy en index...")
    context ={}
    return render(request,'html/index.html',context)


def contacto(request):#contacto
    
    context ={}
    return render(request,'html/contacto.html',context)

def lista_productos(request):#listado productos
    
    context ={"listaProductosMain":listaProductosMain}
    return render(request,'html/nuestrosProductos.html',context)

def nosotros(request):# nosotros
    
    context ={}
    return render(request,'html/acerca de nosotros.html',context)

def ers(request):# ers 
    
    context ={}
    return render(request,'html/ers.html',context)

def compra(request):# compra
    
    context ={}
    return render(request,'html/compra.html',context)

def detalle(request,producto_id):
    
    if request.method == "POST":
        # Recolectar valores de los campos ocultos...
        idProd = request.POST.get("idProducto")
<<<<<<< Updated upstream
=======
        precio = request.POST.get("precio")
        stock = request.POST.get("stock")
        foto = request.POST.get("foto")
        descripcion = request.POST.get("descripcion")
>>>>>>> Stashed changes
        cantidad = request.POST.get("cantidad")

        opc=request.POST.get("opc")
        for producto in listaProductosMain:
            if producto.id==producto_id:
                context={"producto":producto}
                break
        if opc=="Agregar al Carrito":
<<<<<<< Updated upstream
                 
            listaCarrito.append(Carrito(idProd,producto.precio,producto.stock,producto.foto,producto.descripcion,cantidad))
            context={"listaCarrito":listaCarrito}

            for itemCarrito in listaCarrito:
                codigo=int(itemCarrito.id)
                for itemCarrito_list in listaProductosMain:
                    if itemCarrito_list.id==codigo:
                        itemCarrito_list.stock=int(itemCarrito_list.stock)-int(cantidad)
                        break
=======
            

            listaCarrito.append(Carrito(idProd,precio,stock,foto,descripcion,cantidad))
            
            context={"listaCarrito":listaCarrito}
>>>>>>> Stashed changes
            return render(request,'html/carrito.html',context)
    return render(request,'html/detalleProd.html',context)

def carrito(request):
    context={"listaCarrito":listaCarrito}
    return render(request,'html/carrito.html',context)

def vaciar_carro(request):
<<<<<<< Updated upstream
    listaCarrito.clear()
=======
    listaCarrito=[]
>>>>>>> Stashed changes
    context={"listaCarrito":listaCarrito}
    return render(request,'html/carrito.html',context)
#configuracion de inicio de sesion
usuarios = [
{'username': 'mati', 'password': '123'},
{'username': 'alonso', 'password': '123'},
]

#imports


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        
        for usuario in usuarios:
            if usuario['username'] == username and usuario['password'] == password:
                request.session['username'] = username  
                return redirect('index')  

        error_message = 'Nombre de usuario o contraseña incorrectos.'
        return render(request, 'html/login.html', {'error': error_message})
    else:
        return render(request, 'html/login.html')


def logout_view(request):
    logout(request)
    request.session.clear()  
    return redirect('login')
